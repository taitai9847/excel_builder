## ExcelBuilder
読み込んだ CSV ファイルの値を使用して、対象となる Excel ファイルに値を入力するツール。

### 概要
#### Input
Input とするのは下記ファイル。

- base.xlsx
コピー元となる Excel ファイル
- input.csv
出力する Excel ファイルに入力する値を格納するファイル
- input_template.csv
template を用いて Excel ファイルを出力するときに使用する。
- input_template_value.csv
input.csv にマッピングする用の入力値。

#### Output
- 新規で作成する場合
output ディレクトリに Excel ファイルが複数(1つ以上)出力される。

- 既存ファイルに追記する場合
output ディレクトリに対象ファイルを格納しツールを実行する。
ツール実行後、期待した値が入力されているかを確認する。

### How To Use
#### 実行前に確認すること
- 前回の input.csv が残っていないこと
- output ディレクトリに前回のファイルが残っていないこと
- log ディレクトリに前回のファイルが残っていないこと

#### 実行
```bash
# 1. テンプレートから input.csv を生成する
$ python3 main.py template

# 2. (Optional) input.csv から Excel ファイルを作成する
$ python3 main.py file  

# 3. 作成された Excel ファイルに値を入力する
$ python3 main.py
```

### Quick Start
1. INPUT_TEMPLATE_FILE と INPUT_TEMPLATE_VALUE_FILE を用意する。
```bash
$ mv sample_input_template_value.csv input_template_value.csv
$ mv sample_input_template.csv input_template.csv
```

2. コピー元となる BASE_EXCEL_FILE を用意し、config.py の値を更新する。

3. input.csv を生成する。
```bash
$ python3 main.py template
```

4. (Optional) 新規でファイルを作成し、それに値を入力する場合は下記を実行する。
```bash
$ python3 main.py file
```

5. input.csv の値を元に Excel ファイルに値を入力していく。
```bash
$ python3 main.py
```
