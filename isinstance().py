
''' Yaptığın bir programda farzedelim kullanıcıdan bir değer alıcaksınız, 
int veya str olduğunu isinstance ile öğrenip if-elif bloklarında kullanabilirsin.
 Ama type metodunu kullanamazsın bu bloklarda. 
 Ancak iç içe geçmiş verilerin tipini veya herhangi bir veri tipini öğrenebilirsin type ile örneğin int-str-set-frozenset-list-tuple gibi '''

def verial(veri):
	if isinstance(veri, int):#eğer veri intiger ise
		print(veri + veri)
	elif isinstance(veri, str):#eğer veri string ise
		print("string türünde veri girdiniz...")
	else:#eğer başka bir veri tipi ise
		print("girdiğiniz veri tipi : ", type(veri))

verial(1)#intiger ise kendisiyle toplicak
verial("e")#string deniyelim
verial([1])#liste veya başka bir veri tipi