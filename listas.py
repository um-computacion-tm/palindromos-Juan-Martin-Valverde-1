import unittest
def is_palindrome (palabra):
    palabra = palabra.lower().replace(" ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    return palabra == palabra[::-1]

# Ejemplo de uso:
palabra = "Anita lava la tina"
if is_palindrome(palabra):
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")


class TestPalindrome(unittest.TestCase):
   
    def test_a(self):
        resultado = is_palindrome('a')
        self.assertEqual(resultado, True)

    def test_b(self):
        resultado = is_palindrome('B')
        self.assertEqual(resultado, True)

    def test_aa(self):
        resultado = is_palindrome('aa')
        self.assertEqual(resultado, True)

    def test_ab(self):
        resultado = is_palindrome('ab')
        self.assertEqual(resultado, False)

    def test_aCa(self):
        resultado = is_palindrome('aCa')
        self.assertEqual(resultado, True)

    def test_aCs(self):
        resultado = is_palindrome('aCs')
        self.assertEqual(resultado, False)

    def test_ABBA(self):
        resultado = is_palindrome('ABBA')
        self.assertEqual(resultado, True)

    def test_ABCA(self):
        resultado = is_palindrome('BACB')
        self.assertEqual(resultado, False)

    def test_ABCBA(self):
        resultado = is_palindrome('ABCBA')
        self.assertEqual(resultado, True)

    def test_ABCCBA(self):
        resultado = is_palindrome('ABCCBA')
        self.assertEqual(resultado, True)

    def test_ZBCCBA(self):
        resultado = is_palindrome('ZBCCBA')
        self.assertEqual(resultado, False)

    def test_neuquen(self):
        resultado = is_palindrome('neuquen')
        self.assertEqual(resultado, True)

    def test_neuqueM(self):
        resultado = is_palindrome('neuqueM')
        self.assertEqual(resultado, False)

    def test_neu_quen(self):
        resultado = is_palindrome('neu quen')
        self.assertEqual(resultado, True)

    def test_hannah(self):
        resultado = is_palindrome('hannah')
        self.assertEqual(resultado, True)


    def test_pinga(self):
        resultado =is_palindrome('pinga')
        self.assertEqual(resultado, False)
        
    def test_PInGgA(self):
        resultado = is_palindrome('PInGga')
        self.assertEqual(resultado, False)

            
if __name__ == '__main__':

        

    unittest.main()
    
    
    
    