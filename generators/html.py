def generate(data_list):
    html = '<!DOCTYPE html>' + '\n'
    html += '<html lang="en">' + '\n'
    html += '<head>' + '\n'
    html += '\t' + '<meta charset="UTF-8">' + '\n'
    html += '\t' + '<meta name="viewport" content="width=device-width, initial-scale=1.0">' + '\n'
    html += '\t' + '<meta http-equiv="X-UA-Compatible" content="ie=edge">' + '\n'
    html += '\t' + '<title>Data Generator</title>' + '\n'
    html += '\t' + '<link rel="stylesheet" href="public/bootstrap.css">' + '\n'
    html += '</head>' + '\n'
    html += '<body>' + '\n'
    html += '\t' + '<div class="container">' + '\n'
    html += '\t' * 2 + '<table class="table table-striped">' + '\n'
    html += '\t' * 3 + '<thead>' + '\n'
    html += '\t' * 4 + '<tr>' + '\n'
    header = data_list[0].keys()
    for head in header:
        html += '\t' * 5 + '<th>' + head.capitalize() + '</th>' + '\n'
    html += '\t' * 4 + '</tr>' + '\n'
    html += '\t' * 3 + '</thead>' + '\n'
    html += '\t' * 3 + '<tbody>' + '\n'
    for data in data_list:
            html += '\t' * 4 + '<tr>' + '\n'
            for value in data.values():
                html += '\t' * 5 + '<td>'
                html += value
                html += '</td>' + '\n'
            html += '\t' * 4 + '</tr>' + '\n'
    html += '\t' * 3 + '</tbody>' + '\n'
    html += '\t' * 2 + '</table>' + '\n'
    html += '\t' + '</div>' + '\n'
    html += '</body>' + '\n'
    return html