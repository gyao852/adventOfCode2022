from utility import parseInput
from typing import Set, Any, Optional


class File:
    def __init__(self, name: str, size: int, level: int):
        self.name: str = name
        self.size: int = size
        self.level: int = level

    def __repr__(self) -> str:
        return f"- {self.name} (file, size={self.size})"


class Folder:
    def __init__(self, name: str, level: int, prev: Optional['Folder'] = None):
        self.name: str = name
        self.contents: Set[Any] = set()
        self.level: int = level
        self.prev: Optional['Folder'] = prev
        self.size = 0

    def __repr__(self) -> str:
        rep = f"- {self.name} (dir, size={self.size})\n"
        for item in self.contents:
            rep = rep + (" " * (item.level + 3)) + f"{item}\n"
        return rep.strip()


class Solution:
    DISK_SIZE = 70000000
    UPDATE_SIZE = 30000000

    def file_navigator(self, use_real_input: bool = False, second_problem: bool = False) -> int:
        """
        Populates the filesystem of our input, and returns respective sizes or
        directories to remove for update. The solution uses a 'trie' tree,
        where we have a root node/folder (our "\"), which can have N number of
        children node (of type File or Folder). We keep track of both the
        level, and the size of each File/Folder. We also use a pointer
        called prev that goes from one directory up another level.

        :param use_real_input: bool. Use real data if True, else test data
        :param second_problem: bool. If True then return answer for second part
        :return: str. Str containing the letters of the top of each stack
        """
        level = 0
        fs = Folder("/", level) # 'Root' of 'trie'
        cursor = fs # used to point to where we currently are
        i = 1

        # Parse our input
        lines = parseInput("test.txt") if not use_real_input else parseInput("real.txt")
        lines = lines.split("\n")

        # Iterate each command line by line. Worst case O(N)
        while i < len(lines):
            line = lines[i]
            if line[0] == '$':
                cmd = line[2:4]
                # For list command, save all items
                # to current cursor.contents (which
                # is a set of Folders/Files)
                if cmd == "ls":
                    while i + 1 < len(lines) and lines[i + 1][0] != '$':
                        next_line = lines[i + 1]
                        dir_name = next_line[4:]
                        if next_line[0:3] == 'dir' and dir_name not in cursor.contents:
                            cursor.contents.add(Folder(dir_name, level, cursor))
                        else:
                            size_and_name = next_line.split(" ")
                            if size_and_name[1] not in cursor.contents:
                                cursor.contents.add(File(size_and_name[1], int(size_and_name[0]), level))
                        i += 1
                # For cd, we can assume that the only way to go backwards is
                # via .. (ie. no absolute paths that take us back).
                # If .., then we just move our cursor back up one level with
                # the prev pointer
                # Otherwise, move forward down one level for our cursor
                elif cmd == 'cd':
                    dest = line[5:]
                    if dest == "..":
                        cursor = cursor.prev
                        level -= 1
                    else:
                        level += 1
                        # Here, we are setting cursor to be
                        # the new sub-directory, and cursor.prev
                        # to where we just were
                        for content in cursor.contents:
                            if content.name == dest:
                                tmp = cursor
                                cursor = content
                                cursor.prev = tmp
                        if cursor.name != dest:
                            raise Exception(f"Failed to find dir {dest} in current path: {cursor}")
            else:
                raise Exception(f"Found unexpected command {line}")
            i += 1

        # Populate the sizes via dfs: O(N)
        def populate_directories_sizes(root_folder: Folder) -> int:
            queue = [root_folder]
            dir_size = 0
            while queue:
                folder = queue.pop()
                for item in folder.contents:
                    if type(item) == File:
                        dir_size += item.size
                    else:
                        dir_size += populate_directories_sizes(item)
            root_folder.size = dir_size
            return dir_size
        populate_directories_sizes(fs)

        # Iterate through all nodes via bfs. O(N)
        def find_large_directories(root_folder: Folder, for_second_problem: bool = False) -> int:
            nonlocal fs
            queue = [root_folder]
            res = 0 if not second_problem else float('inf')
            cur_free_space = self.DISK_SIZE - fs.size
            while queue:
                folder = queue.pop()
                for item in folder.contents:
                    if type(item) == File:
                        continue
                    else:
                        if not for_second_problem:
                            if item.size <= 100000:
                                res += item.size
                        else:
                            if cur_free_space + item.size >= self.UPDATE_SIZE:
                                res = min(res, item.size)
                        queue.append(item)
            return res

        # print(fs)  # For printing out directory tree
        return find_large_directories(fs, second_problem)


run = Solution()
print(run.file_navigator(False, False))
print(run.file_navigator(True, False))
print(run.file_navigator(False, True))
print(run.file_navigator(True, True))
