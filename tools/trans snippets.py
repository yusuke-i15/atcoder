lines = []
while(True):
    S = input()
    if S == "qqq":
        break
    lines.append(S)
processed_txt = ""
n_tab = 3
for line in lines:
    replaced_line = line.replace('\"', '\\\"')            # 文書中の「"」を「\"」に置換
    replaced_line = replaced_line.replace("\t", "\\t")    # タブ入力をタブ記号(\t)に置換
    processed_line = '\t' * n_tab + '\"' + replaced_line + '\",\n'  # 行頭に(n_tab)個のタブと「"」を挿入（引数にn_tabを指定しなければ 3個のタブを挿入）
    processed_txt += processed_line                       # 処理済みの行を出力用の文字列に追加

processed_txt += "\""
print("end------------------")
print(processed_txt)