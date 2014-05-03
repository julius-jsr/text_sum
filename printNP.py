
class graph:
    sent_id=0
    phrase=""
    related_id=0
    phrase_id=0
    relation=None
    related_to=[]
    related_with=None



class printn:
    x=0
    y=0
    prevt=0
    vp=0
    pp=0
    np=graph()
    pnp=0
    prevk=0
    col=[]
    flag=bool()
    ppg=None
    vpg=None
    prevg=None
    def print_NP(self,t ,sid,gr,head):
        #print "head fff", head
       
            
        l=[]
        
        try:
            t.node
        except AttributeError:
            if (t[1]=="," or t[1]=="CC"):
                print t[0],
                return head
            elif t[1]==".":
                return head
            else:
                print ""
                print t[0]
                self.flag= False
            #print "error"
            
            return head
        else:
            current=None
            current = graph()
            
            s={}
            s['sent_id']=sid
            current.sent_id= sid
            #for k in t:
            #        current.phrase= current.phrase+" " + k[0]
             #       current.pos= current.pos+" "+k[1]
            s['phrase']=""
                
            
            
            if self.x==1 and self.y==1:
                print ""
                print "       ",
                s['related_with']=""
                if self.prevt!=0:
                    self.prevg.related_to.append(current)
                    current.related_with=self.prevg
                    
                    for k in self.prevt:
                        s['related_with']=  s['related_with'] + " " + k[0]
                        print k[0],
                        l.append(k[0])
                else :
                    print 0,
                if self.pp!=0:
                    current.relation=self.ppg
                    print "       ",
                    s['relation']=""
                    for k in self.pp:
                        s['relation']=s['relation'] +" " +k[0]
                        print k[0],
                        l.append(k[0])
                else :
                     print "       ",
                     print 0,
                print "       ",
                s['phrase']=""
                
                for k in t:
                    s['phrase']= s['phrase']+" " + k[0]
                    
                    
                    print k[0],
                    l.append(k[0])
                        #print self.prevt,self.pp,t
                #print ""
                current.phrase=s['phrase']
                self.x=0
                self.y=0
                self.prevt=t
                



                self.prevg=None
                self.prevg=current
                self.prevg.related_to=[]
                for x in current.related_to:
                    self.prevg.related_to.append(x)
                #print s
                if head==None:
                    #print "ooooooooo"
                    
                    head=graph()
                    #print "head", head
                    head.related_to.append(current)
                gr.append(s)
                return head
            
            #print t.leaves()
            if t.node=='NP':
                #print "np is",t
                for k in t:
                    if k[0]!='\'s'and k[0]!='\'':
                         break
                    else:
                        break
                #print self.x,self.y
                #print self.prevk
                if self.x==0:
                    
                    if len(gr)==0 or sid!= gr[-1]['sent_id'] :
                        print ""
                    
                    fl=1
                    if len(gr)>0 and sid== gr[-1]['sent_id'] :
                        self.np=None
                        self.np=self.prevg
                        for k in t:

                            print k[0],
                        
                            ab=gr[-1]
                            ab['phrase']= ab['phrase']+" " + k[0]
                            gr.remove(gr[-1])
                            gr.append(ab)
                            self.np.phrase=ab['phrase']
                        l.append(k[0])
                        self.prevk=k[0]
                        current=self.np

                        #print " yes"
                    else:
                        #print "No"
                        self.np= None
                        self.np= graph()
                        self.np.sent_id=sid
                        for k in t:
                            self.np.phrase=self.np.phrase + " " + k[0]
                        fl=0
                        
        
                        l.append(k[0])
                        self.prevk=k[0]
                        current=None
                        current=self.np
                        current.related_to=[]
                        print self.np.related_to
                        for x in self.np.related_to:
                            current.related_to.append(x)
                    print self.np.phrase,
                    
                    if head==None:
                        if fl==0:
                            self.np.related_to=[]
                        current=None
                        current=self.np
                        current.related_to=[]
                        print self.np.related_to
                        for x in self.np.related_to:
                            current.related_to.append(x)
                        #print "ooooooooo"
                        head=graph()
                        #print "head", head
                        head.related_to=[]
                       
                        #print "first",head.related_to[0].phrase
                       # print "last",head.related_to[-1].phrase
                    
                    self.Flag= True
                    print "current phrase",current.phrase
                    head.related_to.append(current)
                else:
                    self.flag= True
                    s={}
                    s['sent_id']=sid
                   # print ""
                    print "       ",
                    if self.y==0:
                        
                       # print s
                        
                        if self.np.phrase!="":
                            s['related_with']=self.np.phrase
                            
                            current.related_with=self.np
                            print self.np.phrase,
                        else :
                            print "",
                        if self.vp!=0:
                            s['relation']=""
                            print "       ",
                            current.relation=self.vpg
                            for k in self.vp:
                                s['relation']= s['relation'] + " " +k[0]
                                print k[0],
                                l.append(k[0])
                                self.prevk=k[0]
                        else :
                            print "       ",
                            print 0,
                        print "       ",
                        
                        s['phrase']=""
                        for k in t:
                            s['phrase']=s['phrase']+" "+k[0]
                            print k[0],
                            l.append(k[0])
                            self.prevk=k[0]
                        current.phrase=s['phrase']
                        gr.append(s)
                        self.np.related_to.append(current)
                        #print self.np,self.vp,t
                        self.x=0
                        self.y=0
                    else:
                        s['phrase']=""
                        for k in t:
                            s['phrase']=s['phrase']+" "+k[0]
                            print k[0],
                            l.append(k[0])
                            self.prevk=k[0]
                        current.phrase=s['phrase']
                        
                    if head==None:
                        head=graph()
                         #   print "head", head
                    
                        #head.related_to.append(current)
                    
                        
                
                    
                    head.related_to.append(current) 
                self.prevt=t
                
                


                self.prevg=None
                self.prevg=current
                self.prevg.related_to=[]
                for x in current.related_to:
                    self.prevg.related_to.append(x)

                  
                #self.pnp=t
                self.col.append(l)
                #print "head phrase", head.related_to[0].phrase
                return head
            else:
                
                if t.node=='VP':
                    #print self.x,self.y
                    print ""
                    print "       ",
                    if self.np.phrase!="":
                        print self.np.phrase,
                    print "       ",
                    
                    for k in t:
                        current.phrase= current.phrase+" " + k[0]
                        print k[0],
                        l.append(k[0])
                        self.prevk=k[0]
                    print ""
                    
                    self.x=1
                    self.y=0
                    self.vp=t
                    
                    #self.np=self.pnp                    
                    self.prevt=t
                    if head==None:
                            #print "ooooooooo"
                            head=graph()
                            #print "head", head
                            head.related_to.append(current)
                    self.vpg=None
                    self.vpg=current
                    self.vpg.related_to=[]
                    for x in current.related_to:
                        self.vpg.related_to.append(x)
                    self.prevg=None
                    self.prevg=current
                    self.prevg.related_to=[]
                    for x in current.related_to:
                        self.prevg.related_to.append(x)
                    self.col.append(l)
                elif t.node=='PP':
                    if self.x==1 and self.y==0:
                        
                        s['sent_id']=sid
                        s['phrase']=""
                        for k in self.vp:
                            s['phrase']=s['phrase']+" "+k[0]
                            #print k[0],
                            l.append(k[0])
                            self.prevk=k[0]
                        
                        self.vpg.related_with=self.np
                    
                
                        s['related_with']= self.np.phrase
                        
                        self.np.related_to.append(self.vpg)
                        
                        gr.append(s)
                    if head==None:
                            #print "ooooooooo"
                            #print "head", head
                            head=graph()
                            head.related_to.append(current)
                        
                    self.pp=t
                    for k in t:
                        current.phrase= current.phrase+" " + k[0]
                    self.ppg=None
                    self.ppg=current
                    self.ppg.related_to=[]
                    for x in current.related_to:
                        self.ppg.related_to.append(x)
                    self.x=1
                    self.y=1
                    print ""
                    
                #print "other"
                else:
                    head1=0
                    for child in t:
                        head=self.print_NP(child,sid,gr,head)
                    
                #print "head l", head
        return head
        
    
                
