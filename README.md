# ディレクトリ構造リスト生成ツール

このスクリプトは、指定したフォルダ内のすべてのファイルとディレクトリを再帰的にリストアップし、その構造をテキストファイルに出力します。特定のディレクトリ（例：`node_modules`、`.git`など）をスキップして、不要なファイルを出力から除外することができます。

具体的な使用例として、プロジェクトの構成をChatGPTにテキストで送信して解説してもらうなどが挙げられます。

## 特徴

- 指定したフォルダ内のすべてのファイルとディレクトリを再帰的にリストアップ
- `node_modules`、`.git`、`.next`などの特定のディレクトリをスキップ
- わかりやすいツリー形式でディレクトリ構造を出力

## インストール

1. **リポジトリをクローン**:
    ```bash
    git clone https://github.com/yourusername/directory-structure-lister.git
    cd directory-structure-lister
    ```

2. **Pythonがインストールされていることを確認**:
    このスクリプトはPython 3.xが必要です。Pythonは[公式サイト](https://www.python.org/downloads/)からダウンロードできます。

## 使用方法

1. **スクリプトを実行**:
    ```bash
    python list_files.py
    ```

2. **フォルダのパスを入力**:
    プロンプトが表示されたら、対象フォルダの絶対パスまたは相対パスを入力します。例:
    ```plaintext
    フォルダのパスを入力してください: /Users/neromehiro/hiro folder/my_Works/programing/aimsales-website
    ```

3. **出力を確認**:
    ディレクトリ構造はスクリプトと同じディレクトリにある `folder_structure.txt` に書き込まれます。

## 出力例

出力は以下のようになります:

```plaintext
aimsales-website
│
├── pnpm-lock.yaml
├── jsconfig.json
├── tailwind.config.js
├── LICENSE
├── next.config.js
├── next-env.d.ts
├── README.md
├── .gitignore
├── package-lock.json
├── package.json
├── tsconfig.json
├── postcss.config.js
└── /types
    ├── brand.ts
    └── blog.ts
```

## カスタマイズ

### 追加のディレクトリをスキップ

追加でスキップしたいディレクトリがある場合、`list_files.py`スクリプト内の `SKIP_DIRS` セットにディレクトリ名を追加します:

```python
SKIP_DIRS = {
    'node_modules', '.next', '.git', '.idea', '.vscode', '__pycache__', 'dist', 'build', 'coverage', 'logs', 'new_skip_directory'
}
```

### 出力ファイル名の変更

出力ファイル名を変更するには、`list_files.py`スクリプト内の `output_file` 変数を変更します:

```python
output_file = "your_custom_output_file.txt"
```

## コントリビュート

コントリビュートは歓迎します！プルリクエストをお待ちしております。

1. **リポジトリをフォーク**:
2. **新しいブランチを作成**:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. **変更をコミット**:
    ```bash
    git commit -m "Add your commit message here"
    ```
4. **ブランチにプッシュ**:
    ```bash
    git push origin feature/your-feature-name
    ```
5. **プルリクエストを作成**:

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。詳細は[LICENSE](LICENSE)ファイルを参照してください。

## 連絡先

質問や提案がある場合は、Issueを作成するか、[neromehiro@gmail.com](mailto:neromehiro@gmail.com) までご連絡ください。
