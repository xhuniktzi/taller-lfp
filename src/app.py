from os import startfile
from jinja2 import Environment, FileSystemLoader, select_autoescape
from automata import automata

if __name__ == '__main__':
    file = open('./entrada.txt', encoding='utf-8')
    content = file.read()
    tokens, errs = automata(content)

    env = Environment(loader=FileSystemLoader('src/templates'),
                      autoescape=select_autoescape(['html']))

    template = env.get_template('symbol_table.html')
    html_file = open('output.html', 'w+', encoding='utf-8')
    html_file.write(template.render(tokens=tokens, errs=errs))
    html_file.close()

    startfile('output.html')
