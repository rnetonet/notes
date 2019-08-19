VARIAVEL_DO_MODULO = "SPAM!"


def funcao_do_modulo():
    print("eggs!")


class ExemploEscopo:
    def execute(self):
        print(f"Acessando coisas no namespace: {__name__}")
        print(VARIAVEL_DO_MODULO)
        funcao_do_modulo()

        variavel_local = "bacon!"

        print(f"locals(): {locals()}")
        print(f"globals(): {globals()}")
