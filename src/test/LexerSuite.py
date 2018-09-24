import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier_single_char_upcase(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("A","A,<EOF>",101))
    def test_identifier_single_char_lowcase(self):
        self.assertTrue(TestLexer.test("a","a,<EOF>",102))
    def test_identifier_more_char(self):
        self.assertTrue(TestLexer.test("AAAA","AAAA,<EOF>",103))
    def test_identifier_underline(self):
        self.assertTrue(TestLexer.test("_aaaa","_aaaa,<EOF>",104))
    def test_identifier_upcase_lowcase_1(self):
        self.assertTrue(TestLexer.test("Acbbdc","Acbbdc,<EOF>",105))
    def test_identifier_upcase_lowcase_2(self):
        self.assertTrue(TestLexer.test("aA","aA,<EOF>",106))
    def test_identifier_with_number(self):
        self.assertTrue(TestLexer.test("1234aas45vn","1234,aas45vn,<EOF>",107))
    def test_identifier_with_other_char(self):
        self.assertTrue(TestLexer.test("a_as,uio","a_as,,,uio,<EOF>",108))
    def test_identifier_with_other_char_1(self):
        self.assertTrue(TestLexer.test("<=preOP","<=,preOP,<EOF>",109))
    def test_identifier_with_other_char_2(self):
        self.assertTrue(TestLexer.test("< =9preOP","<,=,9,preOP,<EOF>",110))
        # add more tests with _
    def test_integer_pure(self):
        """test integers"""
        self.assertTrue(TestLexer.test("001","001,<EOF>",111))
    def test_integer_with_id(self):
        self.assertTrue(TestLexer.test("001A","001,A,<EOF>",112))
    def test_real_1(self):
        """test reals"""
        self.assertTrue(TestLexer.test("001.2","001.2,<EOF>",113))
    def test_real_pure(self):
        self.assertTrue(TestLexer.test("1.2","1.2,<EOF>",114))
    def test_real_null_right(self):
        self.assertTrue(TestLexer.test("1.","1.,<EOF>",115))
    def test_real_null_left(self):
        self.assertTrue(TestLexer.test(".1",".1,<EOF>",116))
    def test_real_with_exponent(self):
        self.assertTrue(TestLexer.test("1e2","1e2,<EOF>",117))
    def test_real_with_exponent_and_signed_1(self):
        self.assertTrue(TestLexer.test("1.2E-2","1.2E-2,<EOF>",118))
    def test_real_with_exponent_and_signed_2(self):
        self.assertTrue(TestLexer.test("1.2e-2","1.2e-2,<EOF>",119))
    def test_real_null_left_at_fractional_part(self):
        self.assertTrue(TestLexer.test(".1E2",".1E2,<EOF>",120))
    def test_real_no_digit_after_e(self):
        self.assertTrue(TestLexer.test("9.0e","9.0,e,<EOF>",121))
    def test_real_null_fractional_part(self):
        self.assertTrue(TestLexer.test("12e8","12e8,<EOF>",122))
    def test_real_with_exponent_and_signed_3(self):
        self.assertTrue(TestLexer.test("0.33E-3","0.33E-3,<EOF>",123))
    def test_real_no_decimal_point(self):
        self.assertTrue(TestLexer.test("128e-42","128e-42,<EOF>",124))
    def test_comment_pure(self):
        """test comments"""
        self.assertTrue(TestLexer.test("//123","<EOF>",125))
    def test_comment_nested_1(self):
        self.assertTrue(TestLexer.test("//(*abc*)","<EOF>",126))
    def test_comment_nested_2(self):
        self.assertTrue(TestLexer.test("//{abc}","<EOF>",127))
    def test_comment_nested_3(self):
        self.assertTrue(TestLexer.test("//(*abc","<EOF>",128))
    def test_comment_nested_4(self):
        self.assertTrue(TestLexer.test("(*abc*)","<EOF>",129))
    def test_comment_nested_5(self):
        self.assertTrue(TestLexer.test("(*//abc*)","<EOF>",130))
    def test_keyword_1(self):
        self.assertTrue(TestLexer.test("program break s","program,break,s,<EOF>",131))
    def test_keyword_2(self):
        self.assertTrue(TestLexer.test("proCeDure BReak S","proCeDure,BReak,S,<EOF>",132))
    def test_operator_1(self):
        self.assertTrue(TestLexer.test("<>","<>,<EOF>",133))
    def test_operator_2(self):
        self.assertTrue(TestLexer.test(":==not",":=,=,not,<EOF>",134))
    def test_string_1(self):
        """test strings"""
        self.assertTrue(TestLexer.test(r""" "abc" """,r"abc,<EOF>",135))
    def test_string_pure(self):
        self.assertTrue(TestLexer.test(r""" "abc\nabc" """,r"abc\nabc,<EOF>",136))
    def test_string_with_illegal_escape(self):
        self.assertTrue(TestLexer.test(r""" "abc\aabc" """ ,r"Illegal Escape In String: abc\a",137))
    def test_string_with_legal_escape(self):
        self.assertTrue(TestLexer.test(r""" "abc\nabc" """,r"abc\nabc,<EOF>",138))
    def test_string_has_backslash_at_the_end(self):
        self.assertTrue(TestLexer.test(r""" "abc\" """,r"Unclosed String: abc\" ",139))
    def test_string_with_illegal_escape_2(self):
        self.assertTrue(TestLexer.test(r""" "ab\"c" """,r"ab\"c,<EOF>",140))
    def test_string_has_undefined_char(self):
        self.assertTrue(TestLexer.test(r""" "a$bc" """,r"a$bc,<EOF>",141))
    def test_string_has_double_quote_inside(self):
        self.assertTrue(TestLexer.test(r""" "ab"c" """,r"ab,c,Unclosed String:  ",142))
    def test_string_9(self):
        self.assertTrue(TestLexer.test(r""" "ab\\c" """,r"ab\\c,<EOF>",143))
    def test_string_10(self):
        self.assertTrue(TestLexer.test( r""" "\"\n\f\ """,r"Illegal Escape In String: \"\n\f\ ",144 ))
    def test_string_11(self):
        self.assertTrue(TestLexer.test(r""" "var d:array [1 .. 5] of integer;""","Unclosed String: var d:array [1 .. 5] of integer;",145))
    def test_string_12(self):
        self.assertTrue(TestLexer.test(""" "var d:array [1 .. 5]\n of integer;""","Unclosed String: var d:array [1 .. 5]\n",146))           ### \n co nam trong solution k?
    def test_string_13(self):
        self.assertTrue(TestLexer.test(r""" "abc """,r"Unclosed String: abc ",147))
    def test_string_14(self):
        self.assertTrue(TestLexer.test(r""" ""\n\f\n" """,""",Error Token \\""",148 ))
    def test_error_token_1(self):
        self.assertTrue(TestLexer.test( "abc $ 2%4",'abc,Error Token $',149 ))
    def test_array_1(self):
        """test array"""
        self.assertTrue(TestLexer.test("array [ 1 .. 5 ] of integer","array,[,1,..,5,],of,integer,<EOF>",150))
    def test_array_var(self):
        self.assertTrue(TestLexer.test("var d:array [ abc .. 5 ] of integer","var,d,:,array,[,abc,..,5,],of,integer,<EOF>",151))
    def test_array_var_2(self):
        self.assertTrue(TestLexer.test("var d:array [1 .. 5] of integer;","var,d,:,array,[,1,..,5,],of,integer,;,<EOF>",152))
    def test_express_1(self):
        self.assertTrue(TestLexer.test( "(1+a[1]+(1<0))[10] := 4;",'(,1,+,a,[,1,],+,(,1,<,0,),),[,10,],:=,4,;,<EOF>',153 ))    
    def test_express_2(self):
        self.assertTrue(TestLexer.test( "(1>=0)[2] := 2+a[1][1]+c+(\"abc\"< 0);",'(,1,>=,0,),[,2,],:=,2,+,a,[,1,],[,1,],+,c,+,(,abc,<,0,),;,<EOF>',154 ))    
    def test_express_3(self):
        self.assertTrue(TestLexer.test( "d := c [a] + b ;",'d,:=,c,[,a,],+,b,;,<EOF>',155 ))
    def test_statement_if(self):
        self.assertTrue(TestLexer.test("if (x > 3) then x = x + 1;","if,(,x,>,3,),then,x,=,x,+,1,;,<EOF>",156))    
    def test_statement_with(self):
        self.assertTrue(TestLexer.test( """with e , f : integer ; do begin
                        foo2(e,f,"anc");""",'with,e,,,f,:,integer,;,do,begin,foo2,(,e,,,f,,,anc,),;,<EOF>',157 ))
    def test_statement_3(self):
        self.assertTrue(TestLexer.test( """BEGIN
                    with a , b : integer ; do
                        foo2(a,b,"abccc");
                   END""","""BEGIN,with,a,,,b,:,integer,;,do,foo2,(,a,,,b,,,abccc,),;,END,<EOF>""",158 ))
    def test_statement_4(self):
        self.assertTrue(TestLexer.test( """for j:=m+1 doWnTO 100 do beGin
                            s := s + 1;
                            if(a=1) then s:=s-1;
                        eND""","""for,j,:=,m,+,1,doWnTO,100,do,beGin,s,:=,s,+,1,;,if,(,a,=,1,),then,s,:=,s,-,1,;,eND,<EOF>""",159 ))
    def test_statement_call(self):
        self.assertTrue(TestLexer.test( """foo(3,a+1,x and then y,a[1],foo(1,2)[m+1]);""","""foo,(,3,,,a,+,1,,,x,and,then,y,,,a,[,1,],,,foo,(,1,,,2,),[,m,+,1,],),;,<EOF>""",160 ))
    def test_statement_mix(self):
        self.assertTrue(TestLexer.test( """
                proceDure Hello(a, b:integer);
                begin
                    a := b + c;
                    writeln("Hello, world!");
                end
                ""","""proceDure,Hello,(,a,,,b,:,integer,),;,begin,a,:=,b,+,c,;,writeln,(,Hello, world!,),;,end,<EOF>""",161 ))
    def test_statement_7(self):
        self.assertTrue(TestLexer.test( "a := b[10] := foo()[3] := x := 1 ;",'a,:=,b,[,10,],:=,foo,(,),[,3,],:=,x,:=,1,;,<EOF>',162 ))
    def test_statement_8(self):
        self.assertTrue(TestLexer.test( """proceDure main( beGin end""",'proceDure,main,(,beGin,end,<EOF>',163 ))
    def test_statement_mix_2(self):
        self.assertTrue(TestLexer.test( """while(i<n) do begin
                  If(A[i] < A[i-1]) Then
                   Flag :=False; { stop }
                  i:=i+1;
                 end""",'while,(,i,<,n,),do,begin,If,(,A,[,i,],<,A,[,i,-,1,],),Then,Flag,:=,False,;,i,:=,i,+,1,;,end,<EOF>',164 ))
    def test_statement_10(self):
        self.assertTrue(TestLexer.test( "foo(3 ,a+1,m(2));",'foo,(,3,,,a,+,1,,,m,(,2,),),;,<EOF>',165 ))
    def test_simple_procedure_1(self):
        self.assertTrue(TestLexer.test("""proceDure main( beGin end""","proceDure,main,(,beGin,end,<EOF>",166))
    def test_complex_procedure_2(self):
        self.assertTrue(TestLexer.test("""PROCEDURE main() ;
                  var a, b, c : integer ;
                    d: array [1 .. 5] of integer ;
                    e , f : real ;
                  BEGIN
                  END""","""PROCEDURE,main,(,),;,var,a,,,b,,,c,:,integer,;,d,:,array,[,1,..,5,],of,integer,;,e,,,f,:,real,;,BEGIN,END,<EOF>""",167))
    def test_simple_program_3(self):
        self.assertTrue(TestLexer.test("""FUNcTION foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
                  var x,y: real ;
                  BEGIN
                  END""","""FUNcTION,foo,(,a,,,b,:,integer,;,c,:,real,),:,array,[,1,..,2,],of,integer,;,var,x,,,y,:,real,;,BEGIN,END,<EOF>""",168))
    def test_simple_program_4(self):
        self.assertTrue(TestLexer.test("""proCeduRe foo(a, b: integer ; c: real) ;
                  var x,y: real ;
                  BEGIN
                  END""","""proCeduRe,foo,(,a,,,b,:,integer,;,c,:,real,),;,var,x,,,y,:,real,;,BEGIN,END,<EOF>""",169))
    def test_simple_program_5(self):
        self.assertTrue(TestLexer.test("""proCeduRe foo(a, b: integer ; c: real) ;
                  var x,y: real ;
                  BEGIN
                    a := 1;
                    b := a[12] ;
                  END""","""proCeduRe,foo,(,a,,,b,:,integer,;,c,:,real,),;,var,x,,,y,:,real,;,BEGIN,a,:=,1,;,b,:=,a,[,12,],;,END,<EOF>""",170))
    def test_simple_program_6(self):
        self.assertTrue(TestLexer.test("""proCeduRe foo(c: real) ;
                   var x,y: real ;
                   BEGIN
                    1 := 1;
                    c := a[12] ;
                   END""","""proCeduRe,foo,(,c,:,real,),;,var,x,,,y,:,real,;,BEGIN,1,:=,1,;,c,:=,a,[,12,],;,END,<EOF>""",171))
    def test_complex_program_1(self):
        self.assertTrue(TestLexer.test("""function foo(c: real): real ;
                   var x,y: array[m..n] of real;
                   BEGIN
                    a[m+n] := a[m+1] ;
                    foo()[m*1] := a[a div 3] ;
                   END""","""function,foo,(,c,:,real,),:,real,;,var,x,,,y,:,array,[,m,..,n,],of,real,;,BEGIN,a,[,m,+,n,],:=,a,[,m,+,1,],;,foo,(,),[,m,*,1,],:=,a,[,a,div,3,],;,END,<EOF>""",172))
    def test_complex_program_with_multi_assign(self):
        self.assertTrue(TestLexer.test("""function foo(c: real): real ;
                   var x: integer ;
                   BEGIN
                    a[m+n] := a[m+1] := foo()[m*1] := a[a div 3] := (a>m) and then (b<n);
                   END""","""function,foo,(,c,:,real,),:,real,;,var,x,:,integer,;,BEGIN,a,[,m,+,n,],:=,a,[,m,+,1,],:=,foo,(,),[,m,*,1,],:=,a,[,a,div,3,],:=,(,a,>,m,),and,then,(,b,<,n,),;,END,<EOF>""",173))
    def test_simple_program_with_assign_statement(self):
        self.assertTrue(TestLexer.test("""function foo(c: real): real ; x:=a[1]""","""function,foo,(,c,:,real,),:,real,;,x,:=,a,[,1,],<EOF>""",174))
    def test_simple_program_10(self):
        self.assertTrue(TestLexer.test("""function foo(c: real): real ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                   END""","""function,foo,(,c,:,real,),:,real,;,var,x,:,real,;,BEGIN,if,(,a,>,1,),then,a,:=,1,;,END,<EOF>""",175))
    def test_complex_program_with_if_statement(self):
        self.assertTrue(TestLexer.test("""function foo(b : array [1 .. 2] of integer ) : array [2 .. 3] of real;
                                        var a : array [ 2 .. 3 ] of real;
                                        begin
                                        if () then return a; //CORRECT
                                        else return b; //WRONG
                                        end""","""function,foo,(,b,:,array,[,1,..,2,],of,integer,),:,array,[,2,..,3,],of,real,;,var,a,:,array,[,2,..,3,],of,real,;,begin,if,(,),then,return,a,;,else,return,b,;,end,<EOF>""",176))
    def test_keyword_no_space_1(self):
        self.assertTrue(TestLexer.test("thelineisnotBREAKANDnospace","thelineisnotBREAKANDnospace,<EOF>",177)) #is ID
    def test_keyword_no_space_2(self):
        self.assertTrue(TestLexer.test("well BreAK iskeyword","well,BreAK,iskeyword,<EOF>",178))
    def test_keyword_with_other_1(self):
        self.assertTrue(TestLexer.test("keyword continue to test with \n endline","keyword,continue,to,test,with,endline,<EOF>",179))
    def test_keyword_with_other_2(self):
        self.assertTrue(TestLexer.test("keyword has more \\n is legal","keyword,has,more,Error Token \\",180))
    def test_real_with_multi_decimal_dot(self):
        self.assertTrue(TestLexer.test("1.1.1","1.1,.1,<EOF>",181))
    def test_real_with_multi_decimal_dot_and_exponent_and_signed(self):
        self.assertTrue(TestLexer.test("1.1.1e-1","1.1,.1e-1,<EOF>",182))
    def test_real_with_multi_decimal_dot_and_exponent(self):
        self.assertTrue(TestLexer.test("1.1.1e","1.1,.1,e,<EOF>",183))
    def test_string_with_escape_in_both_side(self):
        self.assertTrue(TestLexer.test("\"\\fabc\\n\" ",r"\fabc\n,<EOF>",184))
    def test_keyword_with_illegalEscape_and_legalEscape(self):
        self.assertTrue(TestLexer.test("\"\\nillegalAndLegal\\x\" ",r"Illegal Escape In String: \nillegalAndLegal\x",185))
    def test_keyword_with_illegalEscape_in_both_side(self):
        self.assertTrue(TestLexer.test("\"\\yillegalAndLegal\\x\" ","Illegal Escape In String: \y",186))
    
    def test_error_token_percent_1(self):
        self.assertTrue(TestLexer.test( r'%','Error Token %',187 ))
    
    def test_error_token_more_percent(self):
        self.assertTrue(TestLexer.test( r'% %','Error Token %',188 ))
    
    def test_error_token_and_nonerror_token(self):
        self.assertTrue(TestLexer.test( 'non error token &','non,error,token,Error Token &',189 ))
    
    def test_error_token_and_nonerror_token_2(self):
        self.assertTrue(TestLexer.test( 'non error token & error token','non,error,token,Error Token &',190 ))
    
    def test_error_token_dot(self):
        self.assertTrue(TestLexer.test( '.','Error Token .',191 ))
    
    def test_error_token_with_backslash_and_a_character(self):
        self.assertTrue(TestLexer.test( r'\a','Error Token \\',192 ))
    
    def test_boolean_expression_1(self):
        self.assertTrue(TestLexer.test( 'true > false','true,>,false,<EOF>',193 ))
    def test_boolean_expression_2(self):
        self.assertTrue(TestLexer.test( 'TRue >= FALSe','TRue,>=,FALSe,<EOF>', 194))
    def test_error_token_with_id_inside(self):
        self.assertTrue(TestLexer.test("thisID^andErrorToken","thisID,Error Token ^",195))
    def test_error_token_with_id(self):
        self.assertTrue(TestLexer.test("thisID@","thisID,Error Token @",196))
    def test_complex_expression_1(self):
        self.assertTrue(TestLexer.test("a[m+n] = a[m+1] := foo()[m*1] := a[a div 3] := (a>m) and then (b<n);","a,[,m,+,n,],=,a,[,m,+,1,],:=,foo,(,),[,m,*,1,],:=,a,[,a,div,3,],:=,(,a,>,m,),and,then,(,b,<,n,),;,<EOF>",197))
    def test_complex_expression_2(self):
        self.assertTrue(TestLexer.test("a[m+true] = a[b[2]+1] := foo()[m*1] := a[a div 3] := (a>=m) and then (b<=n);","a,[,m,+,true,],=,a,[,b,[,2,],+,1,],:=,foo,(,),[,m,*,1,],:=,a,[,a,div,3,],:=,(,a,>=,m,),and,then,(,b,<=,n,),;,<EOF>",198))
    def test_boolean_expression_with_ADDOP(self):
        self.assertTrue(TestLexer.test( '1+1+1+1+1+1','1,+,1,+,1,+,1,+,1,+,1,<EOF>', 199))
    def test_boolean_expression_with_ADDOP_BOOL(self):
        self.assertTrue(TestLexer.test( '1+1+1+1+1+1=5','1,+,1,+,1,+,1,+,1,+,1,=,5,<EOF>', 200))
    