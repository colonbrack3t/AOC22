rawdata = open("day7input","r").read()
total_space = 70000000
unused_space = 30000000
target_space = total_space - unused_space
min_directory_size_to_delete = total_space # temporarily impossible
closest_directory_size = 70000000
data = rawdata.split('\n')
dirs_less_than_100000_sum = 0
class Node:
    name = ''
    is_folder = False
    sub_files = []
    size = 0
    def getSize(self):
        if self.is_folder:
            size =  sum([n.getSize() for n in self.sub_files])
            if size < 100000:
                global dirs_less_than_100000_sum
                dirs_less_than_100000_sum += size
            global min_directory_size_to_delete
            global closest_directory_size
            if size >= min_directory_size_to_delete and size < closest_directory_size:
                closest_directory_size = size

            return size
        else:
            return self.size
    def __init__(self,name, is_folder, size):
        self.name = name
        self.is_folder = is_folder
        if is_folder:
            self.sub_files = []
        else:
            self.size = size
    def get_subfile(self, sub_file_name):
        if not self.is_folder:
            print ('ERRORRR')
        for f in self.sub_files:
            if f.name == sub_file_name:
                return f
    def add_subfile(self, sub_file, path):
        if not self.is_folder:
            print ('ERRORRR')
        if len(path) == 0:
            self.sub_files.append(sub_file)
        else:
            sub_folder_name = path[0]
            
            self.get_subfile(sub_file_name=sub_folder_name).add_subfile(sub_file,path[1:])
    def __str__(self):
        if self.is_folder:
            subs = ''.join([n.__str__() +'\n' for n in self.sub_files])
            return f'{self.name} : [' '\n'+ subs + ']'
        else:
            return f'{self.name} : {self.size}'
filesystem = Node('/', True,0)
curr_command = 'none'
curr_dir = []
for d in data:
    if d[0] == '$':
        command = d[2:].split(' ')
        if command[0] == 'ls':
            curr_command = 'ls'
        if command[0] == 'cd':
            curr_command = 'cd'
            _, new_dir = command
            if new_dir == '..':
                curr_dir.pop()
            elif new_dir == '/':
                curr_dir = []
            else:
                curr_dir.append(new_dir)
    else:
        if curr_command == 'ls':
            line = d.split(' ')
            n = None
            if line[0] == 'dir':
                n = Node(line[1],True,0)

            else:
                n = Node(line[1],False, int(line[0]))
            filesystem.add_subfile(n,curr_dir)

            



min_directory_size_to_delete = filesystem.getSize() - target_space
print(f'\033[91m{dirs_less_than_100000_sum}')
filesystem.getSize()
print(closest_directory_size)