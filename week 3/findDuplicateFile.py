def findDuplicateFile(self, paths: list[str]) -> list[list[str]]:
    content_map = {}
    
    for path in paths:
        parts = path.split()
        directory = parts[0]
        
        for file_info in parts[1:]:
            name, content = file_info.split('(')
            content = content[:-1]
            
            if content not in content_map:
                content_map[content] = []
            content_map[content].append(f"{directory}/{name}")
    
    return [file_paths for file_paths in content_map.values() if len(file_paths) > 1]