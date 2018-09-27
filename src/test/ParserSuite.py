import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_function_DECLARE_non_upcase(self):
        input ="""
            procedure foo();
            begin
                while trUE do 
                begin
                    bar();
                end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_function_DECLARE_upcase(self):
        """FUNCTION foo(a,b: integer; g: real; j:array [1 .. 5] of real):array [5 .. 7] of integer;
                  var x,y,z,k: real ;

                  BEGIN

                  END"""
        input = """FUNCTION foo(a,b: integer; g: real; j:array [1 .. 5] of real):array [5 .. 7] of integer;
                  var x,y,z,k: real ;

                  BEGIN

                  END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 202))

    def test_statement_ASSIGN_single(self):
        """proCeduRE foo(m, n: integer; c: real) ;
                  var x,y,z: real ;
                  BEGIN
                    m := 12; n := c[2];
                  END"""
        input = """proCeduRE foo(m, n: integer; c: real) ;
                  var x,y,z: real ;
                  BEGIN
                    m := 12;
                    n := c[2];
                    z := n;
                    m := z;
                  END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_statement_wrong_FUNCTION(self):
        """function foo_ASSIGN_with_index_express(c: real): real ; y:=a[0]"""
        input = """function foo_ASSIGN_with_index_express(c: real): real ; y:=a[0]"""
        expect = "Error on line 1 col 56: y"

        self.assertTrue(TestParser.test(input, expect, 204))

    def test_statement_ASSIGN_with_FUNCCALL(self):
        """PROCeduRe ASSIGN_with_FUNCCALL() ;
                  var x,y,z: real ;
                  BEGIN
                    a := "char";  b := func(1,a+1) ;
                  END"""
        input = """PROCeduRe ASSIGN_with_FUNCCALL() ;
                  var x,y,z: real ;
                  BEGIN
                    a := "char";  b := func(1,a+1) ;
                  END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_statement_ASSIGN_with_wrong_LHS(self):
        """proCEDURE ASSIGN_with_wrong_LHS(c: real) ;
                   var y,z: real ;
                   BEGIN
                    2 := 1;
                    c := a[0] ;
                   END"""
        input = """proCEDURE ASSIGN_with_wrong_LHS(c: real) ;
                   var y,z: real ;
                   BEGIN
                    2 := 1;
                    c := a[0] ;
                   END"""
        expect = "Error on line 4 col 22: :="

        self.assertTrue(TestParser.test(input, expect, 206))

    def test_statement_ASSIGN_with_LOWER_BOUND_is_express(self):
        """function ASSIGN_with_more_index_express(c: real): real ;
                   var x,y: array[m..n] of real;
                   BEGIN
                    a[m+n] := a[n+1] := 1 ;
                   END"""
        input = """function ASSIGN_with_more_index_express(c: real): real ;
                   var x,y: array[m..n] of real;
                   BEGIN
                    a[m+n] := a[n+1] := 1 ;
                   END"""
        expect = "Error on line 2 col 34: m"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_statement_ASSIGN_with_index_express_of_FUNCCALL(self):
        """FUNCTION ASSIGN_with_index_express_of_FUNCCALL(c: integer): integer ;
                   var x,y: integer;
                   BEGIN
                    a[m+n] := a[m+1] := foo()[m*2] := a[2 div a] := (a>=m)
                    and then (b<=n);
                   END"""
        input = """FUNCTION ASSIGN_with_index_express_of_FUNCCALL(c: integer): integer ;
                   var x,y: integer;
                   BEGIN
                    a[m+n] := a[m+1] := foo()[m*2] := a[2 div a] := (a>=m)
                    and then (b<=n);
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_statement_ASSIGN_with_missing_COBOUND(self):
        """function ASSIGN_with_missing_COBOUND(c: real): real ; x:=a[1]"""
        input = """function ASSIGN_with_missing_COBOUND(c: real): real ; x:=a[1]"""
        expect = "Error on line 1 col 54: x"

        self.assertTrue(TestParser.test(input, expect, 209))

    def test_statement_with_IF_statement(self):
        """function IF_statement(c: integer): real ;
                   var y,z:real ;
                   BEGIN
                    if(a>=1) then a:=1 ;
                    if a=1 then return;
                   END"""
        input = """function IF_statement(c: integer): real ;
                   var y,z:real ;
                   BEGIN
                    if(a>=1) then a:=1 ;
                    if a=1 then return;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 210))

    def test_statement_with_IF_ELSE_nested(self):
        """pROCEDURE IF_ELSE_nested(c: integer) ;
                   var y:real ;
                   BEGIN
                    if(a>=1) then a:=1 ;
                    else if (1<=2)<>(2<=3)
                        then x:=2 ;
                    else foo(a+1,1);
                   END"""
        input = """pROCEDURE IF_ELSE_nested(c: integer) ;
                   var y:real ;
                   BEGIN
                    if(a>=1) then a:=1 ;
                    else if (1<=2)<>(2<=3)
                        then x:=2 ;
                    else foo(a+1,1);
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_statement_with_more_IF(self):
        """pROCEDURE more_IF(c: real) ;
                   var x:real ;

                   BEGIN
                    if(a>=1) then a:=2 ;
                    if (1<=2) then beGIN x:=2 ; eND
                    else foo(a+1,2);
                    if (1) then return;
                   END"""
        input = """pROCEDURE more_IF(c: real) ;
                   var x:real ;

                   BEGIN
                    if(a>=1) then a:=2 ;
                    if (1<=2) then beGIN x:=2 ; eND
                    else foo(a+1,2);
                    if (1) then return;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 212))

    def test_statement_IF_with_COBOUND(self):
        """pROCEDURE IF_with_COBOUND(c: real) ;
                   var x:real ; z: integer;

                   BEGIN
                    if(a>=1) then a:=0 ;
                    if (1<=2) then beGIN x:=1 ;
                        enD
                    else IF_with_COBOUND(a+1,a);
                   END"""
        input = """pROCEDURE IF_with_COBOUND(c: real) ;
                   var x:real ; z: integer;

                   BEGIN
                    if(a>=1) then a:=0 ;
                    if (1<=2) then beGIN x:=1 ;
                        enD
                    else IF_with_COBOUND(a+1,a);
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 213))

    def test_statement__nested_IF_with_COBOUND(self):
        """pROCEDURE nested_IF_with_COBOUND(c: string) ;
                   var x:real ; z: integer;

                   BEGIN
                    if(a>=1) then beGin
                        a:=1 ;
                        if(2=1) then
                        a:= b[1];
                        else b:=a[1]:= 1;
                    ENd
                    END"""
        input = """pROCEDURE nested_IF_with_COBOUND(c: string) ;
                   var x:real ; z: integer;

                   BEGIN
                    if(a>=1) then beGin
                        a:=1 ;
                        if(2=1) then
                        a:= b[1];
                        else b:=a[1]:= 1;
                    ENd
                    END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 214))

    def test_statement_WITH(self):
        """pROCEDURE WITHstm(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [2 .. 4] of real ; dO
                    d := c[a] + b ;
                   END"""
        input = """pROCEDURE WITHstm(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [2 .. 4] of real ; dO
                    d := c[a] + b ;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 215))

    def test_statement_WITH_with_COBOUND(self):
        """pROCEDURE WITH_with_COBOUND(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do begin
                    a := c[a] + b ;
                    foo();WITH_with_COBOUND(a,b,c);

                    end
                   END"""
        input = """pROCEDURE WITH_with_COBOUND(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do begin
                    a := c[a] + b ;
                    foo();WITH_with_COBOUND(a,b,c);

                    end
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 216))

    def test_statement_WITH_with_CALL_statement(self):
        """pROCEDURE WITH_with_CALL_statement(c: real) ;
                   BEGIN
                    with a ,b : integer ; c: array [1 .. 2] of real ; do
                    begin
                    d := c [a] + b ;
                    foo();WITH_with_CALL_statement(a,b,c);
                    with a , b : integer ; do
                    begin
                        WITH_with_CALL_statement(a,b,"abc");
                    end
                    end
                   END"""
        input = """pROCEDURE WITH_with_CALL_statement(c: real) ;
                   BEGIN
                    with a ,b : integer ; c: array [1 .. 2] of real ; do
                    begin
                    d := c [a] + b ;
                    foo();WITH_with_CALL_statement(a,b,c);
                    with a , b : integer ; do
                    begin
                        WITH_with_CALL_statement(a,b,"abc");
                    end
                    end
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 217))

    def test_statement_nested_WITH(self):
        """function nested_WITH(d: real): sTRIng;
                   BEGIN
                    with c , d : integer ; c : array [1 .. 2] of real ; do
                    with a , b : integer ;
                    do
                        nested_WITH(a,b,"anc");
                   END"""
        input = """function nested_WITH(d: real): sTRIng;
                   BEGIN
                    with c , d : integer ; c : array [1 .. 2] of real ; do
                    with a , b : integer ;
                    do
                        nested_WITH(a,b,"anc");
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 218))

    def test_statement_FOR(self):
        """function statement_FOR(c: real): STRIng;
                   BEGIN
                    FOR i:=1 to m+10
                    do
                        s := s + 1;
                        m := s;
                   END"""
        input = """function statement_FOR(c: real): STRIng;
                   BEGIN
                    FOR i:=1 to m+10
                    do
                        s := s + 1;
                        m := s;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 219))

    def test_statement_WITH_and_FOR(self):
        """function foo(c: real): STRIng;
                   BEGIN
                    with i, j: integer; tmp: real; do
                    print(i, j, tmp);
                    FOR i:=1 to m+10
                    do
                        s := s + 1;
                   END"""
        input = """function foo(c: real): STRIng;
                   BEGIN
                    with i, j: integer; tmp: real; do
                    print(i, j, tmp);
                    FOR i:=1 to m+10
                    do
                        s := s + 1;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 220))

    def test_statement_WHILE_single(self):
        """PROCEDURE foo(c: integer) ;
                   var x:real ;
                   BEGIN
                    WhILe(a<>1) do beGin end
                   END"""
        input = """PROCEDURE foo(c: integer) ;
                   var x:real ;
                   BEGIN
                    WhILe(a<>1) do beGin end
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 221))

    def test_statement_WHILE_and_IF(self):
        """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a=1) do beGin
                        if(a=1) then x:=1;
                        foo();
                    end
                   END"""
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a=1) do beGin
                        if(a=1) then x:=1;
                        foo();
                    end
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 222))

    def test_statement_nested_WHILE(self):
        input = """pROCEDURE foo(d: real) ;
                   BEGIN
                    "2"[4]:=d;
                    END
                    """
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 223))

    def test_statement_NESTED_WHILE_and_IF(self):
        """pROCEDURE foo(d: real) ;
                   BEGIN
                    whILe(a<>1) do bEGin
                        while(1) do x:=1;
                        if(a=1) then
                        begin end
                    end
                   END"""
        input = """pROCEDURE foo(d: real) ;
                   BEGIN
                    whILe(a<>1) do bEGin
                        while(1) do x:=1;
                        if(a=1) then
                        begin end
                    end
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 224))

    def test_statement_nested_WHILE_and_IF_and_COBOUND(self):
        """pROCEDURE foo(d: real) ;
                   BEGIN
                    whILe(1) do bEGin
                        while(1) do x:=1;
                        if(a=1) then
                        begin end
                    end
                   END"""
        input = """pROCEDURE foo(d: real) ;
                   BEGIN
                    whILe(1) do bEGin
                        while(1) do x:=1;
                        if(a=1) then
                        begin end
                    end
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 225))

    def test_statement_nested_WHILE_and_ASSIGN(self):
        """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a<>1) do BEGin
                        while(1) do x:=1;
                        x := x + 1;
                    end
                   END"""
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a<>1) do BEGin
                        while(1) do x:=1;
                        x := x + 1;
                    end
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 226))

    def test_statement_FOR_2(self):
        """function foo(s: real): STRIng;
                   BEGIN
                    FOR j:=0 to m+10
                    do begin
                        s := s + 1; end
                   END"""
        input = """function foo(s: real): STRIng;
                   BEGIN
                    FOR i:=1 to m+10
                    do
                        s := s + 1;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 227))

    def test_statement_FOR_with_IF(self):
        """function foo(c: real): sTRIng;
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        s := s + 1;
                        c := i;
                        if(a=1) then begin s:=s-1; end
                    end
                   END"""
        input = """function foo(c: real): sTRIng;
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        s := s + 1;
                        if(a=1) then begin s:=s-1; end
                    end
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 228))

    def test_statement_nested_FOR(self):
        """function foo(d: real): STRIng;
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        for j:=m+1 doWnTO 100 do bEGin
                            s := s + 3;
                            d := s := i;
                            if(a=1) then s:=s-1;
                        eND
                    end
                   END"""
        input = """function foo(d: real): STRIng;
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        for j:=m+1 doWnTO 100 do bEGin
                            s := s + 3;
                            d := s := i;
                            if(a=1) then s:=s-1;
                        eND
                    end
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 229))

    def test_statement_nested_FOR_WHILE_FOR(self):
        """PROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        while i>1 do
                            FOR i:=m+1 doWnTO 10 do
                                while j>1 do x:=foo(10);
                                print(j);
                    End
                   END"""
        input = """PROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        while i>1 do
                            FOR i:=m+1 doWnTO 10 do
                                while j>1 do x:=foo(10);
                                print(j);
                    End
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_statement_with_BREAK(self):
        """pROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        print(i);
                        brEaK;
                    end
                   END"""
        input = """pROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        print(i);
                        brEaK;
                    end
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 231))

    def test_statement_BREAK2(self):
        """pROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        brEaK;
                    end
                    break;
                   END"""
        input = """pROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        brEaK;
                    end
                    break;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 232))

    def test_statement_CONTINUE(self):
        """PROCEDURE foo(c: real);
                   BEGIN
                    while (1) do ContinuE ;
                   END"""
        input = """PROCEDURE foo(c: real);
                   BEGIN
                    while (1) do ContinuE ;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 233))

    def test_statement_RETURN(self):
        """pROCEDURE foo(c: real);
                   BEGIN
                    while (1) do RETURN ;
                   END"""
        input = """pROCEDURE foo(c: real);
                   BEGIN
                    while (1) do RETURN ;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 234))

    def test_statement_CALL(self):
        """function statement_CALL(c: real): real;
                   BEGIN
                    statement_CALL(3,a+1,a<>1,a[1]);
                    return 1;
                   END"""
        input = """function statement_CALL(c: real): real;
                   BEGIN
                    statement_CALL(3,a+1,a<>1,a[1]);
                    return 1;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 235))

    def test_statement_nested_CALL(self):

        input = """function foo(c: real): integer;
                   BEGIN
                    y := foo(3,foo(foo1(foo(2,a+1))));
                    return func(a(1,2));
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 236))

    def test_statement_nested_WITH_CALL(self):
        """function foo(c: real): integer;
                   BEGIN
                    foo (3,a+1);
                    foo1();
                    return;
                   END"""
        input = """function foo(c: real): integer;
                   BEGIN
                    foo (3,a+1);
                    foo1();
                    return;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 237))

    def test_statement_CALL_with_COMMENT(self):
        """function foo(c: real): integer;
                   BEGIN
                    text(insert); { colour}
                	{.comment here.}
                    return func(a(1,2));
                   END"""
        input = """function foo(c: real): integer;
                   BEGIN
                    text(insert); { colour}
                	{.comment here.}
                    return func(a(1,2));
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 238))

    def test_statement_CALL_with_more_parameter(self):
        """function foo(c: real): integer;
                   BEGIN
                    foo(3,a+1,x and then y, c,a[1],foo(1,2)[m+1]);
                    return foo2() + foo() + 1;
                   END"""
        input = """function foo(c: real): integer;
                   BEGIN
                    foo(3,a+1,x and then y, c,a[1],foo(1,2)[m+1]);
                    return foo2() + foo() + 1;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 239))

    def test_statement_MIX_ASSIGMENT(self):
        """
        procedure test1() ;
        begin
            if a=b then
            bEGin
                    b := c := 6;
                    if(e <> f) then foo(a,c) else a := b := c ;
            end
        end
        """
        input = """
                procedure test1() ;
                begin
	               if a=b then
	               bEGin
		                 b := c := 6;
		                 if(e <> f) then foo(a,c); else a := b := c ;
	               end
                end
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,240))

    def test_statement_mix_IF_WHILE(self):
        """
                procedure test_mix_if_while() ;
                begin
	               if a=b then if c=d then while (d=e) do
                   beGin
                        if (1) then print("OK");
                   eND
               else c := 1;
                end
                """
        input = """
                procedure test_mix_if_while() ;
                begin
	               if a=b then if c=d then while (d=e) do
                   beGin
                        if (1) then print("OK");
                   eND
               else c := 1;
                end
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,241))
    def test_statement_mix_VAR_FUNCTION_PROCEDURE(self):
        """
                VAR i: real ;
                FUNCTION funcmix(): integer ;
                begin
	               return 100;
                end
                procedure procmix() ;
                var
	               m: integer ;
                begin
	               m := f() ;  
                   put(m);
	               put(main);
                end
                var g: real ;
                """
        input = """
                VAR i: real ;
                FUNCTION funcmix(): integer ;
                begin
	               return 100;
                end
                procedure procmix() ;
                var
	               m: integer ;
                begin
	               m := f() ;  
                   put(m);
	               put(main);
                end
                var g: real ;
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,242))

    def test_statement_PROCEDURE(self):
        """
                proceDure Hello(b:integer);
                begin
                    a := b := b + c;
                end
                """
        input = """
                proceDure Hello(b:integer);
                begin
                    a := b := b + c;
                end
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,243))
    def test_statement_FUNCTION(self):
        """
        var x, y: real;

        function add(x, y: real): real;
        
        begin
            return x + y + random();
        end
        """
        input = """
        var x, y: real;

        function add(x, y: real): real;
        
        begin
            return x + y + random();
        end
        """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,244))
    def test_statement_WRONG_OPERATOR(self):
        """
        function add(x, y: real): real;
        
        begin
        if a < b then
        begin 
            a := 1;
            b = foo(a); 
        end
        end
        """
        input = """
        function add(x, y: real): real;
        
        begin
        if a < b then
        begin 
            a := 1;
            b = foo(a); 
        end
        end
        """
        expect = "Error on line 8 col 14: ="

        self.assertTrue(TestParser.test(input,expect,245))
    def test_statement_ASSIGN_with_nested_index_express(self):
        """
                procedure mainfoo() ;
                beGin
                 a[b[2]] := 100;
                 foo(2);
                 return ;
                eND
                """
        input = """
                procedure mainfoo() ;
                beGin
                 a[b[2]] := 100;
                 foo(2);
                 return ;
                eND
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,246))
    def test_statement_mix_more_ELSE(self):
        """
                PROCEDURE main() ;
                beGin
                 if a=b then 
                 if c = d then e := f;
                 else i := 1;
                 else x := 2 ;
                eND
                """
        input = """
                PROCEDURE main() ;
                beGin
                 if a=b then 
                 if c = d then e := f;
                 else i := 1;
                 else x := 2 ;
                eND
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,247))
    def test_statement_mix_complex_FOR_statement(self):
        """
                procedure swap() ;
                var a: array[0 .. m-1] of integer;
                 i,j,temp: integer;
                beGin
                    for i := 0 to n do
                        for j:= i+1 to n-1 do
                            if(a[i]>a[j]) then
                            beGin
                            temp := a[i];
                            a[i] := a[j];
                            a[j] := temp;
                            eND
                    print(a);
                eND
                """
        input = """
                procedure swap() ;
                var a: array[0 .. 1] of integer;
                 i,j,temp: integer;
                beGin
                    for i := 0 to n do
                        for j:= i+1 to n-1 do
                            if(a[i]>a[j]) then
                            beGin
                            temp := a[i];
                            a[i] := a[j];
                            a[j] := temp;
                            eND
                    print(a);
                eND
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,248))
    def test_statement_mix_IF_with_COMMENT(self):
        """
        procedure swap() ;
        var a: array[0 .. m-1] of integer;
            i,j,temp: integer;
        beGin
        { 
            if then else
        }
        function("hello");
        eND
        """
        input = """
        procedure swap() ;
        var a: array[0 .. m-1] of integer;
            i,j,temp: integer;
        beGin
        { 
            if then else
        }
        function("hello");
        eND
        """
        expect = "Error on line 3 col 26: m"

        self.assertTrue(TestParser.test(input,expect,249))
    def test_statement_WRONG_EXPRESSION_of_IF(self):
        """
        procedure swap() ;
        var a: array[0 .. 1] of integer;
            i,j,temp: integer;
        beGin
        if (x:=1) = 2 then
            print("done");
        else
            exit(0);
        END
        """
        input = """
        procedure swap() ;
        var a: array[0 .. 1] of integer;
            i,j,temp: integer;
        beGin
        if (x:=1) = 2 then
            print("done");
        else
            exit(0);
        END
        """
        expect = "Error on line 6 col 13: :="

        self.assertTrue(TestParser.test(input,expect,250))

    def test_statement_RETURN_EXPRESSION(self):
        """
        Function CountX(A:array[0 .. 100] of integer; N,X : Integer) : Integer;
        Var i , Count : Integer;
        Begin
            Count := 0;
            For i:=1 to N do
            If ( A[i] = X ) then
            Count := Count + 1;
            return Count;
        End
        """
        input = """
                Function CountX(A:array[0 .. 100] of integer; N,X : Integer) : Integer;
                Var i , Count : Integer;
                Begin
                 Count := 0;
                 For i:=1 to N do
                  If ( A[i] = X ) then
                   Count := Count + 1;
                 return Count;
                End
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,251))

    def test_statement_index_expression_in_IF(self):
        """
        PROCEDURE replace (A:array[0 .. 100] of integer;N, x,y:Integer);
        Var i:Integer;
        Begin
        For i:=0 to N do
        If(A[i] = y) then { x ==> y }
        A[i] := x;
        return;
        End
        """
        input = """
                Procedure replace (A:array[0 .. 100] of integer;N, x,y:Integer);
                Var i:Integer;
                Begin
                 For i:=0 to N do
                  If(A[i] = x) then { x ==> y }
                  A[i] := y;
                  return;
                End
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,252))

    def test_statement_mix_FUNCCALL_as_IF_EXPRESSION(self):
        """
            function calc(i : integer): boolean;
            var k : integer;
            begin
            if copy(s,i-2*k+1,k) = copy(s,i-k+1,k) then
                begin
                exit();
                end
            end
        """
        input = """
                function calc(i : integer): boolean;
                var k : integer;
                begin
                if copy(s,i-2*k+1,k) = copy(s,i-k+1,k) then
                   begin
                    exit();
                   end
                end
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,253))
    def test_statement_PROCEDURE_missing_var_declare(self):
        
        input = """
                Var R,S,P:real;
                pROCEDURE Scalc() ;
                Begin
                    Read(R);
                    S := 3.14 * R * R;
                    P := 2 * 3.14 * R;
                    return;
                End
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,254))
    
    def test_statement_mix_complicated_EXPRESSION(self):
        input = """
                Var R,S,P:real;
                pROCEDURE Scalc() ;
                Begin
                    Read(R);
                    S := 3.14 * R * R;
                    P := 2 * 3.14 * R;
                    Mul := (S*P) / (S+P);
                    return Mul;
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))
    
    def test_UNCLOSED_COMMENT(self):
        
    
        """ Test ... """
        input ="""
        var a, b, c: real;
        var x, y, z: Boolean;
        

        function n(): Real;
        var x, y, z: Integer;
        begin
            readLn();
            fs := readStdin();
            
            with i: integer; do begin
                for i := 6 downto -1 do h := 6 + i;
                if i > 6 then return 0;
            end
            return 1;
        end
        var w : integer;

        function bj(): Boolean;
        var a: string;
        begin 
            (*       
        end
        """
        expect ="Error on line 23 col 13: *"
        self.assertTrue(TestParser.test(input,expect,256))
       
    def test_statement_mix_IF_with_VAR_DECLARE(self):
        """ Function Min(N:Integer) :Integer;
                Var x,y:Integer;
                Begin
                    if x <= y then i := x; else i := y;
                End"""
        input = """ Function Min(N:Integer) :Integer;
                Var x,y:Integer;
                Begin
                    if x <= y then i := x; else i := y;
                End"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,257))
    def test_statement_mix_nested_IF_with_RETURN_and_nested_index_expression(self):
        """
                procedure main() ;
                beGin
                 a[b[2]] := 10;
                 foo();
                 if a=b then if c = d then e := f;
                 else i := 1;
                 else x := 2 ;
                 return ;
                eND
                """
        input = """
                procedure main() ;
                beGin
                 a[b[2]] := 10;
                 foo();
                 if a=b then if c = d then e := f;
                 else i := 1;
                 else x := 2 ;
                 return ;
                eND
                """
        expect = "successful"
        

        self.assertTrue(TestParser.test(input,expect,258))
    def test_statement_mix_IF_with_nested_COBOUND_and_CALL(self):
        """
                procedure test() ;
                begin
	               if a=b then
	               begin
		                 b := c ;
		                 if(e <> f) then foo(a,c) ;
                    if a=b then if c=d then while (d=e) do
                   beGin
                   eND
	               end
                end
                """
        input = """
                procedure test() ;
                begin
	               if a=b then
	               begin
		                 b := c ;
		                 if(e <> f) then foo(a,c) ;
                    if a=b then if c=d then while (d=e) do
                   beGin
                   eND
	               end
                end
                """
        expect = "successful"
        

        self.assertTrue(TestParser.test(input,expect,259))
    def test_statement_mix_VAR_DECLARE_and_PROCEDURE(self):
        """
                Var name: String;
                Procedure Main();
                Begin
	               (*this is line*)
	               writeln();//this is new line}
	               writeln(name);
	               readln();
                End
                """
        input = """
                Var name: String;
                Procedure Main();
                Begin
	               (*this is line*)
	               writeln();//this is new line}
	               writeln(name);
	               readln();
                End
                """
        expect = "successful"
        

        self.assertTrue(TestParser.test(input,expect,260))

    def test_statement_RETURN_with_EXPRESSION_FUNCCALL(self):
        
        input = """
                function gt(x:integer):integer;
                begin
                if x = 0 then
                 return 1;
                else
                 return x*gt(x-1);
                end
                """
        expect = "successful" 
        

        self.assertTrue(TestParser.test(input,expect,261))
    def test_statement_FUNCCALL_as_EXPRESSION(self):
        """
                function fibonacy(x: integer): integer;
                var f1,f2: integer;
                temp: integer;
                Begin
                 if x<=2 then
                  return 1;
                 else
                  temp := fibonacy(x-2)+ fibonacy(x-1);
                  return temp;
                end
                """
        input = """
                function fibonacy(x: integer): integer;
                var f1,f2: integer;
                temp: integer;
                Begin
                 if x<=2 then
                  return 1;
                 else
                  temp := fibonacy(x-2)+ fibonacy(x-1);
                  return temp;
                end
                """
        expect = "successful"
        

        self.assertTrue(TestParser.test(input,expect,262))
    def test_statement_FUNCCALL_as_FUNCCALL_parament(self):
        """function foo(c: real; d: integer): integer;
                   BEGIN
                    c := d;
                    return c;
                    foo(foo());
                   END"""
        input = """function foo(c: real; d: integer): integer;
                   BEGIN
                    c := d;
                    return c;
                    foo(foo());
                   END"""
        expect = "successful" 
        

        self.assertTrue(TestParser.test(input,expect,263))
    def test_statement_wrong_FUNCCALL(self):
        """function foo(c: real; d:integer): integer;
                   BEGIN
                    c := foo1(c d);
                    return c;
                   END"""
        input = """function foo(c: real; d: foo1(): integer;
                   BEGIN
                    c := foo1(c d);
                    return c;
                   END"""
        expect = "Error on line 1 col 25: foo1" 
        

        self.assertTrue(TestParser.test(input,expect,264))
    
    def test_statement_wrong_FUNCTION_DECLARE(self):
        """function foo(c: real d: integer: integer;
                   BEGIN
                    c := foo1(c, d);
                    return c;
                   END"""
        input = """function foo(c: real d: integer: integer;
                   BEGIN
                    c := foo1(c, d);
                    return c;
                   END"""
        expect = "Error on line 1 col 21: d"  
        

        self.assertTrue(TestParser.test(input,expect,265))
    def test_statement_wrong_IF(self):
        """function foo(c: real; d: integer): integer;
                   BEGIN
                    if () then
                    c := foo1(c, d);
                    return c;
                   END"""
        input = """function foo(c: real; d: integer): integer;
                   BEGIN
                    if () then
                    c := foo1(c, d);
                    return c;
                   END"""
        expect = "Error on line 3 col 24: )" 
        

        self.assertTrue(TestParser.test(input,expect,266))
    def test_statement_wrong_WHILE_COLON_redundant(self):
        input = """function foo(c: real; d: integer): integer;
                   BEGIN
                    while (1) do:
                    c := foo1(c, d);
                    return c;
                   END"""
        expect = "Error on line 3 col 32: :" 
        
        

        self.assertTrue(TestParser.test(input,expect,267))
    def test_statement_wrong_WITH_missing_SEMI(self):
        
        
        input = """function foo(c: real; d: integer): integer;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real  do begin
                    d := c [a] + b ; 
                    
                    return c;
                    end
                   END"""
        expect = "Error on line 3 col 71: do" 

        self.assertTrue(TestParser.test(input,expect,268))
    def test_statement_wrong_COBOUND_missing_END(self):
        
        input = """function foo(c: real; d: integer): integer;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real;  do begin
                    d := c [a] + b ; 
                    
                    return c;
                   END"""
        expect = "Error on line 7 col 22: <EOF>"
        

        self.assertTrue(TestParser.test(input,expect,269))
    def test_statement_wrong_RETURN_missing_SEMI(self):
        
        input = """function foo(c: real; d: integer): integer;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real;  do begin
                    d := c [a] + b ; 
                    end
                    return c
                   END"""
        expect = "Error on line 7 col 19: END" 
        

        self.assertTrue(TestParser.test(input,expect,270))
    def test_statement_wrong_CONTINUE_missing_SEMI(self):
        
        input = """function foo(c: real; d: integer): integer;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real;  do begin
                    d := c [a] + b ; 
                    continue
                    end
                    return c;
                    
                   END"""
        expect = "Error on line 6 col 20: end"
        

        self.assertTrue(TestParser.test(input,expect,271))
    def test_wrong_PROGRAM_STRUCTURE(self):
        
        input = """
                with a , b : integer ; c : array [1 .. 2] of real;  do begin
                    d := c [a] + b ; 
                    continue
                    end
                    return c;
                """
        expect = "Error on line 2 col 16: with"

        self.assertTrue(TestParser.test(input,expect,272))
    def test_statement_wrong_ASSIGN_wrong_operator(self):
        
        input = """function foo(c: real; d: integer): integer;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real;  do begin
                    d = c [a] + b ; 
                    continue;
                    return c;
                    end
                   END"""
        expect = "Error on line 4 col 22: ="
        

        self.assertTrue(TestParser.test(input,expect,273))
    def test_statement_wrong_FOR_missing_expression(self):
        
        input = """function foo(c: real; d: integer): integer;
                   BEGIN
                    for ()  do begin
                    d := c [a] + b ; 
                    continue;
                    return c; end
                   END"""
        expect = "Error on line 3 col 24: ("
        

        self.assertTrue(TestParser.test(input,expect,274))
    def test_statement_CONTINUE_with_WHILE(self):
        
        input = """Procedure testContinue(c: real);
                   BEgin
                    while (1) do coNtInUe ;
                   EnD
                   """
        expect = "successful"
        

        self.assertTrue(TestParser.test(input,expect,275))
    def test_statement_CALL_and_RETURN(self):
        input = """function testCALL(c: real): integer;
                   BEgin
                    testCALL(1,a<>1,a[1]);
                    return 1;
                   EnD
                   """
        expect = "successful"
        

        self.assertTrue(TestParser.test(input,expect,276))
    def test_statement_with_triple_COBOUND(self):
        
        input = """
                Procedure test1() ;
                BEgin
	               if a=b then
	               BEgin
		                 b := c ;
		                 if(e <> f) then begin test1(a,c) ; end
	               EnD
                EnD
                """
        expect = "successful"
        

        self.assertTrue(TestParser.test(input,expect,277))
    def test_statement_wrong_ASSIGN_missing_operand(self):
        
        input = """
                function sum_real_array(a: array[0 .. 10] of real;n:integer):real;
                var i:integer;s:real;
                BEgin
                    a:=:=4;
                     Writeln("Sum of real array: "+sum_real_array(a,n));
                EnD
                """
        expect = "Error on line 5 col 23: :="
        

        self.assertTrue(TestParser.test(input,expect,278))
    def test_statement_MULTI_RETURN(self):
        
        input = """
                function power(x:integer):integer;
                BEgin
                if x = 0 then
                 return 1;
                else
                 return x*power(x-1);
                EnD
                """
        expect = "successful"
        

        self.assertTrue(TestParser.test(input,expect,279))
    def test_statement_more_statement(self):
        
        input = """
                Function test_more_stmt(m,n:integer):integer;
               
                 var a: real;
                  BEgin
                    begin
                        for i := 1 to 10 do 
                        a := a +1;
                        break;                    
					end
                EnD
                """
        expect = "successful"
        

        self.assertTrue(TestParser.test(input,expect,280))
    def test_statement_VAR_DECLARE(self):
        
        input = input = """
                var i: boolean;
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))
    def test_statement_mix_FOR_IF_RETURN(self):
        input = """
                Function testing(): Boolean;
                Var Flag:Boolean;
                    i :Integer;
                BEgin
                 Flag:=True;
                 For  i :=1 to N do
                 If(A[i] <> A[N-i  +1]) Then
                 Flag :=False;     
                 return flag;
                EnD
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,282))
    def test_statement_nested_scope(self):
        input = """
                Function nested_scope(  N :Integer) : Boolean;
                Var Flag : Boolean;
                 i :Integer;
                BEgin
                 begin
                 EnD
                 return Flag;
                EnD
                """
        expect = "successful"
        
        self.assertTrue(TestParser.test(input,expect,283))
    def test_statement_wrong_STATEMENT_after_DO(self):
        input = """
                Procedure test(A: Integer; k, X:Integer);
                Var i :Integer;
                BEgin
                 For i:=N downto k+ 1 do
                  
                EnD
                """
        expect = "Error on line 7 col 16: EnD"

        self.assertTrue(TestParser.test(input,expect,284))
    def test_statement_MULTI_STATEMENT(self):
        
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
        begin 
        x := y + 1 := 1;
        a := y;
        b := a;
        c := a;
        end"""
        expect = "Error on line 4 col 19: :="
        self.assertTrue(TestParser.test(input,expect,285))
      
    def test_statement_wrong_EXPRESSION(self):
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
        begin 
        x := y + 1 := 1;

        end"""
        expect = "Error on line 4 col 19: :="
        self.assertTrue(TestParser.test(input,expect,286))
    def test_statement_complex_ASSIGN_and_RETURN(self):
        """procedure foo(a,b:integer; c:real);
        var x,y: real;
        begin 
        a := b [10] := foo()[3] := x := 1 ;
        return;
        end"""
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
        begin 
        a := b [10] := foo()[3] := x := 1 ;
        return;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))
    def test_statement_WRONG_ASSIGN(self): 
        """procedure foo(a,b:integer; c:real);
        var x,y: real;
        begin 
        a := b [10] := 3 := x := 1 ;
        return;

        end"""
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
        begin 
        a := b [10] := 3 := x := 1 ;
        return;

        end"""
        expect = "Error on line 4 col 25: :="
        self.assertTrue(TestParser.test(input,expect,288))
    def test_statement_ARRAY_DECLARE(self): 
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        x := y + 1;
        y := z[2];
        y := y * y;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))
    def test_statement_FUNCCALL_as_index_express(self): 
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        x := y + 1;
        x := z[2];
        foo(x);
        foo(2)[3+x] := a[b[2]] +3;
        return foo(x);
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))

    def test_statement_IF_THEN(self):     
        """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        if 5>6 then x := y;
        end"""
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        if 5>6 then x := y;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))

    def test_statement_IF_THEN_ELSE(self):       
        """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        if (5>6) then x := y; else y := x := 1;
        
        end"""
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        if (5>6) then x := y; else y := x := 1;
        
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))

       
    def test_statement_nested_IF_with_ASSIGN(self):    
        """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        if (5>6) then x := y; else 
            if (true) then y:=x;
        x := z[2];
        end"""
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        if (5>6) then x := y; else 
            if (true) then y:=x;
        x := z[2];
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))

    
    def test_statement_PROCEDURE_missing_SEMI(self):
        """procedure foo(a,b:integer; c:real);
        var x,y: real
            z: array[2 .. 3] of integer;
        begin 
        if (5>6) then x := y; else 
            if (true) then y:=x;
        
        end"""
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real
            z: array[2 .. 3] of integer;
        begin 
        if (5>6) then x := y; else 
            if (true) then y:=x;
        
        end"""
        expect = "Error on line 3 col 12: z"
        self.assertTrue(TestParser.test(input,expect,294))
    def test_wrong_miss_RB(self):
        """Miss ) """
        input = """procedure foo(a,b:integer; c:real;
        var x,y: real 
        begin
        end"""
        expect = "Error on line 2 col 8: var"
        self.assertTrue(TestParser.test(input,expect,295))

    def test_wrong_miss_SEMI_at_VAR_DECLARE(self):
        """incorrect variable declaration 3"""
        input = """float a,c,d"""
        expect = "Error on line 1 col 0: float"
        self.assertTrue(TestParser.test(input,expect,296))

    def test_ARRAY_DECLARE(self):
        """array type"""
        input = """var d:array [ 1 .. 5 ] of integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))
    def test_array_wrong_miss_RSB(self):        
        input = """var d:array [ 1 .. 5  of integer;"""
        expect = "Error on line 1 col 22: of"
        self.assertTrue(TestParser.test(input,expect,298))
    def test_VAR_DECLARE_with_ARRAY(self):    
        input = """var d:array [1 .. 5] of integer; a,b,c: integer; e,f: real;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))
    def test_array_DECLARE_with_ESCAPE(self):
        input = """var d:array [1 .. 5] of integer;\n a,b,c: integer;\n e,f: real;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))
    def Atest_array_DECLARE_with_ESCAPEs(self):
        input = """ "2"[4]:=d;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,301))
    def test_array_DECLARE_with_ESCAPEss(self):
        input = """
        procedure foo(a,b:integer; c:real);
        begin
        if (b>=a) and (b>=c) then max:=b; end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,302))