# MEMBENTUK SET (versi-1)   MakeSet (L) 

# REALISASI 
MakeSet1(L) : 
 if IsEmpty(L)  then {Basis} 
        L 
 else {Rekurens} 
      if IsMember(FirstElmt(L),Tail(L)) then 
           MakeSet(TAIL(L))   
    else Konso (FirstElmt(L),MakeSet(Tail(L)) 