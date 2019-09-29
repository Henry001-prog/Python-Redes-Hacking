import optparse

parser = optparse.OptionParser()

parser.add_option("-?",action="help",help="MOSTRA A AJUDA")
parser.add_option("-F","--HENRY",help="MOSTRA O NOME DO CANAL",dest="NOME",metavar="NOME CANAL",type="str")

(options, args) = parser.parse_args()

if options.NOME:
	print("Aqui tem um valor",options.NOME)
else:
	print("Não tem valor")
print(options.NOME)
print(args)