import PySimpleGUI as gui
from Cliente import Cliente

class FormCliente:
    def __init__(self):
        conteudo = [
            [ gui.Text("Nome: "), gui.Input (size=(20,10), key = 'txtNome') ] ,
            [ gui.Checkbox("Aceita receber e-mail", key = 'aceitaEmail') ] ,
            [
                gui.Text("Sexo "),
                gui.Radio ("Feminino", 'sexo', key = 'feminino') , gui.Radio("Masculino", ' sexo', key = 'masculino')
            ] ,
            [gui.Text("Idade: "), gui.Slider(range =(0,150), orientation = 'h', key = 'idade', default_value = 18)],
            [gui.Text("Telefone: "), gui.Input(size=(20, 10) ,key='txtTelefone')],
            [
                gui.Text("Estado Civil "),
                gui.Radio("Casado", 'sexo', key='casado'), gui.Radio("Solteiro", 'sexo', key='solteiro'), gui.Radio("Divorciado", 'sexo', key = 'divorciado')
            ],

            [gui.Button("Salvar")]
        ]
        self.tela = gui.Window("Formulário de Produto").layout( conteudo )

    def show(self):
        self.button, self.valores = self.tela.Read()
        cliente = Cliente()
        cliente.nome = self.valores['txtNome']
        cliente.aceitaEmail = self.valores['aceitaEmail']
        cliente.nome = self.valores['txtNome']
        if self.valores['feminino']:
            cliente.sexo = 'feminino'
        elif self.valores ['masculino']:
            cliente.sexo = 'masculino'
        else:
            cliente.sexo = "Não informado"

        cliente.idade = self.valores['idade']
        cliente.telefone = self.valores['txtTelefone']

        if self.valores['casado']:
            cliente.estadoCivil = 'casado'
        elif self.valores ['divorciado']:
            cliente.estadoCivil = 'divorciado'
        elif self.valores ['solteiro']:
            cliente.estadoCivil = 'Solteiro'
        else:
            cliente.estadoCivil = "Não informado"
        return cliente