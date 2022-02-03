import os

separate_files = True
out_dir = '../exercises'
in_file = 'exer_raw.txt'

if __name__ == "__main__":

    os.makedirs(out_dir, exist_ok=True)

    lines = []

    with open(in_file) as infile:

        for n, line in enumerate(infile):
            try:
                line = line.strip()
                if line == "":
                    continue
                elif line.startswith("***"):
                    print(n, line.strip('*'))
                    continue
                if line == "ENDFILE":
                    break
                line = line.split(maxsplit=1)
                prefix = line[0].lower()
                mode = 'exercise'
                source = None
                if prefix in ["note", "title", "text"]:
                    mode = prefix
                else:
                    source = prefix
                    mode = 'exercise'
                content = line[1].replace('\\n', '\n')
                if content.endswith('```'):
                    content = content[:-3] + '\n```python\n'
                    for codeline in infile:
                        content += codeline
                        if '```' in codeline:
                            break
                lines.append({'content': content, 'mode': mode, 'source': source})
            except Exception as e:
                print(n, line, e)

        # TODO read effort level


    # TODO print effort level
    if not separate_files:
        out_filename = f'{out_dir}/exercises.md'

        with open(out_filename, 'w+') as outfile:
            outfile.write("# Python for linguists\n")

    titles = 0
    exercises = 0
    exercises_total = 0
    for line in lines:
        if line['mode'] == 'title':
            titles += 1
            exercises = 0
            string = f'\n\n## {titles}. {line["content"]}'
            if separate_files:
                short_title = line["content"].split('(')[0].strip()
                out_filename = f'{out_dir}/{titles}_{short_title}.md'
                with open(out_filename, 'w+') as outfile:
                    outfile.write("# Python for linguists\n")
        elif line['mode'] == 'note':
            string = f'- - - - - -\n**Something to keep in mind:** {line["content"]}\n- - - - -'
        elif line['mode'] == 'text':
            string = line["content"]
        else:
            exercises += 1
            exercises_total += 1
            string = f'**{titles}.{exercises}.** {line["content"]}'
        with open(out_filename, 'a') as outfile:
            outfile.write(string + '\n\n')

    print('Total exercises:', exercises_total)
