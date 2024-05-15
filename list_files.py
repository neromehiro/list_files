import os

# スキップするディレクトリ名のリスト
SKIP_DIRS = {
    'node_modules', '.next', '.git', '.idea', '.vscode', '__pycache__', 'dist', 'build', 'coverage', 'logs'
}

def list_files_recursive(folder_path, output_file):
    with open(output_file, 'w') as file:
        for root, dirs, files in os.walk(folder_path):
            # スキップするディレクトリを削除
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            level = root.replace(folder_path, '').count(os.sep)
            indent = '│   ' * level
            line = f'{indent}├── {os.path.basename(root)}/\n'
            if level == 0:
                line = f'{os.path.basename(root)}/\n'
            print(line.strip())  # デバッグ用
            file.write(line)
            sub_indent = '│   ' * (level + 1)
            for i, f in enumerate(files):
                file.write(f'{sub_indent}├── {f}\n')

if __name__ == "__main__":
    folder_path = input("フォルダのパスを入力してください: ").strip().strip('\'"')
    if not os.path.isdir(folder_path):
        print("指定されたパスはフォルダではありません。")
    else:
        output_file = "folder_structure.txt"
        list_files_recursive(folder_path, output_file)
        print(f"ファイル構成が {output_file} に出力されました。")
