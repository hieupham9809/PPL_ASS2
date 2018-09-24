from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        templist = []
        for decl in ctx.declaration():
            if decl.varDec():
                templist += self.visit(decl)
            else: templist += [self.visit(decl)]
            #templist += typeDec
        return Program(templist)


    def visitDeclaration(self, ctx:MPParser.DeclarationContext):
        if ctx.varDec():
            return self.visit(ctx.varDec())
        else:
            if ctx.funcDec():
                return self.visit(ctx.funcDec())
            else: return self.visit(ctx.procDec())

    def visitVarDec(self, ctx:MPParser.VarDecContext):
        listOfType = ctx.listOfType()
        listOfVarDecl = []
        for x in listOfType:
            listid, types = self.visit(x)
            
            for id in listid:
                listOfVarDecl.append(VarDecl(id,types))
            #print(i for i in listOfVarDecl)
        return (listOfVarDecl)
        #return self.visit()
    def visitListOfType(self, ctx:MPParser.ListOfTypeContext):
        listid = []
        for listlistid in ctx.ID():
            listid.append(listlistid.getText())
        
        
        return listid,self.visit(ctx.types())

    def visitTypes(self, ctx:MPParser.TypesContext):
        if ctx.BOOLEAN(): return BoolType()
        elif ctx.INTEGER(): return IntType()
        elif ctx.REAL(): return FloatType()
        elif ctx.STRING(): return StringType()
        else: return self.visit(ctx.arraycp())

    def visitArraycp(self, ctx:MPParser.ArraycpContext):
        temp = ""
        if ctx.BOOLEAN(): temp = BoolType()
        elif ctx.INTEGER(): temp = IntType()
        elif ctx.REAL(): temp = FloatType()
        else: temp = StringType()
        
        return ArrayType(IntLiteral(int(ctx.INTLIT(0).getText())),
                        IntLiteral(int(ctx.INTLIT(1).getText())),
                        temp
                                                        )
    def visitFuncDec(self, ctx:MPParser.FuncDecContext):
        name = ctx.ID().getText()
        param = self.visit(ctx.paramList())
        returnType = self.visit(ctx.types())
        local = self.visit(ctx.varDec())
        body = self.visit(ctx.compound_st())
        return FuncDecl(name,param,local,body,returnType)

    def visitProcDec(self, ctx:MPParser.ProcDecContext):
        name = ctx.ID().getText()
        param = self.visit(ctx.paramList())
        local = self.visit(ctx.varDec())
        body = self.visit(ctx.compound_st())
        return FuncDecl(name,param,local,body)
    def visitParamList(self, ctx:MPParser.ParamListContext):
        listOfVarDecl = []
        listOfType = ctx.listOfType()
        if not listOfType:
            return []
        else:
            for x in listOfType:
                listid, types = self.visit(x)
                for id in listid:
                    listOfVarDecl.append(VarDecl(id,types))
            return listOfVarDecl
    def visitCompound_st(self, ctx:MPParser.Compound_stContext):
        statements = ctx.statement()
        statementsList = []
        if not statements:
            return []
        else:
            for statement in statements:
                statementsList.append(self.visit(ctx.statement()))
                '''if statement.assign_st():
                    statementsList.append(self.visit(statement.assign_st()))
                elif statement.if_st():
                    statementsList.append(self.visit(statement.if_st()))
                elif statement.for_st():
                    statementsList.append(self.visit(statement.for_st()))
                elif statement.while_st():
                    statementsList.append(self.visit(statement.while_st()))
                elif statement.break_st():
                    statementsList.append(self.visit(statement.break_st()))
                elif statement.continue_st():
                    statementsList.append(self.visit(statement.continue_st()))
                elif statement.return_st():
                    statementsList.append(self.visit(statement.return_st()))
                elif statement.call_st():
                    statementsList.append(self.visit(statement.call_st()))
                elif statement.compound_st():
                    statementsList.append(self.visit(statement.compound_st()))
                else: 
                    statementsList.append(self.visit(statement.with_st()))'''
        return statementsList

    def visitStatement(self, ctx:MPParser.StatementContext):
        if ctx.assign_st():
            return self.visit(ctx.assign_st())
        elif ctx.if_st():
            return self.visit(ctx.if_st())
        elif ctx.for_st():
            return self.visit(ctx.for_st())
        elif ctx.while_st():
            return self.visit(ctx.while_st())
        elif ctx.break_st():
            return self.visit(ctx.break_st())
        elif ctx.continue_st():
            return self.visit(ctx.continue_st())
        elif ctx.return_st():
            return self.visit(ctx.return_st())
        elif ctx.call_st():
            return self.visit(ctx.call_st())
        elif ctx.compound_st():
            return self.visit(ctx.compound_st())
        else: 
            return self.visit(ctx.with_st())

    
    
'''
    def visitFuncdecl(self,ctx:MPPars
        er.FuncdeclContext):
        local,cpstmt = self.visit(ctx.body()) 
        return FuncDecl(Id(ctx.ID().getText()),
                        [],
                        local,
                        cpstmt,
                        self.visit(ctx.mtype()))

    def visitProcdecl(self,ctx:MPParser.ProcdeclContext):
        local,cpstmt = self.visit(ctx.body()) 
        return FuncDecl(Id(ctx.ID().getText()),
                        [],
                        local,
                        cpstmt)

    def visitBody(self,ctx:MPParser.BodyContext):
        return [],[self.visit(ctx.stmt())] if ctx.stmt() else []
  
    def visitStmt(self,ctx:MPParser.StmtContext):
        return self.visit(ctx.funcall())

    def visitFuncall(self,ctx:MPParser.FuncallContext):
        return CallStmt(Id(ctx.ID().getText()),[self.visit(ctx.exp())] if ctx.exp() else [])

    def visitExp(self,ctx:MPParser.ExpContext):
        return IntLiteral(int(ctx.INTLIT().getText()))

    def visitMtype(self,ctx:MPParser.MtypeContext):
        return IntType()
'''        

