"""
Create a pdf from code in the repository
"""
import os
import re


def read_file(filename):
    contents = ""
    with open(filename, "r") as f:
        contents = f.read()
    return contents


def read_files_list(filename):
    file_list = []
    with open(filename, "r") as f:
        file_list = f.readlines()
    listings = [read_file(x.replace("\n", "")) for x in file_list]
    return listings, file_list


def lstlisting(listings, file_list):
    result = str()
    n = len(listings)
    pattern = re.compile(r"\d{4}_([\w\W]+)\.py")
    curr_chapter = ""
    for i in range(n):
        f_name = file_list[i].replace("\n", "")
        f_name = os.path.split(f_name)
        chapter = f_name[0].replace("./", "")

        if chapter != curr_chapter:
            result += "\\chapter{" + f"{chapter}" + "}\n"
            curr_chapter = chapter

        match_object = pattern.search(f_name[1])
        if match_object:
            f_name_clean = match_object.group(1).replace("_", " ").title()
            result += "\\section{" + f"{f_name_clean}" + "}\n"
            result += ("\\begin{lstlisting}[language=Python]\n" + listings[i] + "\n\\end{lstlisting}\n")
        else:
            f_name_clean = f_name[1].replace("_", " ").title()
            result += "\\section{" + f"{f_name_clean}" + "}\n"
            result += ("\\begin{lstlisting}[language=Python]\n" + listings[i] + "\n\\end{lstlisting}\n")

    return result


def main():
    listings, file_list = read_files_list("file_list.txt")
    lstlistings = lstlisting(listings, file_list)
    tex_code = read_file("format_code.tex") + lstlistings + "\\end{document}"
    with open("code.tex", "w") as f:
        f.write(tex_code)


if __name__ == "__main__":
    main()
