import streamlit as st

def style_gen():
   st.markdown("""
      <style>
      [data-testid="stWidgetLabel"]{
            color: #ff00ff !important;
            font-size: 10px !important;
            font-weight: 400 !important;
            display: flex;
            justify-content: right !important;
         }        
      [role="radiogroup"] {
            display: flex !important;
            justify-content: center !important;
         }
      .st-cc {
            font-size: 12px !important;
            font-weight: 500 !important;
         }
      [data-testid="stRadio"] label:has(input:checked) {
         color: white !important;
         background-color: rgba(200,200,200,.3) !important;
         padding: .4rem .8rem !important;
         border: 1px solid white !important;
         }
      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(3) > div > div > label:nth-child(1) > div.st-ba.st-bp.st-bq.st-br.st-bs.st-bt.st-bu.st-bv.st-bw.st-bx.st-by > div > p{
      color: white !important;
                     }                
      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(3) > div > div > label:nth-child(2) > div.st-ba.st-bp.st-bq.st-br.st-bs.st-bt.st-bu.st-bv.st-bw.st-bx.st-by > div > p{
      color: white !important;
                     }                
      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(3) > div > div > label:nth-child(3) > div.st-ba.st-bp.st-bq.st-br.st-bs.st-bt.st-bu.st-bv.st-bw.st-bx.st-by > div > p{
      color: white !important;
                     }                
      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(3) > div > div > label:nth-child(4) > div.st-ba.st-bp.st-bq.st-br.st-bs.st-bt.st-bu.st-bv.st-bw.st-bx.st-by > div > p{
      color: white !important;
                  }                
   
      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(3) > div > label > div > p{
                  font-size: 20px;
                  font-weight: bold;
                  color: yellow;
                     }
                  
      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(3) > div > label > div > p{
                  font-size: 20px;
                  font-weight: bold;
                  color: yellow;
                     }

      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(4) > div > label > div > p{
                  font-size: 20px;
                  font-weight: bold;
                  color: yellow;
                     }

   #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(5) > div > label > div > p{
               font-size: 20px;
               font-weight: bold;
               color: yellow;
                  }
   #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(4) > div > label > div > p{
               font-size: 20px;
               font-weight: bold;
               color: yellow;
                  }

   #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(6) > div > label > div > p{
               font-size: 20px;
               font-weight: bold;
               color: yellow;
                  }

   #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(7) > div > label > div > p{
               font-size: 20px;
               font-weight: bold;
               color: yellow;
                  }

   #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(8) > div > label > div > p{
               font-size: 20px;
               font-weight: bold;
               color: yellow;
                  }


   #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(1) > div > div > h2{
      font-size: 2rem;
      font-weight: 600;
      color: aqua !important;
      margin: 1rem !important;
                  }

                  
      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(3) > div > div > div > div{
               background-color: rgba(0,0,0,0) !important;                }

      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(3) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > div.st-eg.st-dm.st-c9.st-db.st-da.st-eh{
               color: white !important}               

      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(3) > div > div > div > div > div.st-ak.st-al.st-as.st-da.st-bg.st-db.st-dc > svg{
               color: #00ffff !important;                }                

      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(3) > div > div > div > div > div.st-ak.st-al.st-bd.st-be.st-bf.st-as.st-bg.st-bh.st-ar.st-bi.st-bj.st-bk.st-bl > div.st-eg.st-cn.st-ar.st-ca.st-c9.st-eh{
               color: white !important;                }                

      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(3) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > span{
               background-color: rgba(200,200,200,0.3) !important;                }                
                  

      
      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(4) > div > div > div > div{
               background-color: rgba(0,0,0,0) !important;                }

      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(4) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > div.st-eg.st-dm.st-c9.st-db.st-da.st-eh{
               color: white !important}               }                

      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(4) > div > div > div > div > div.st-ak.st-al.st-as.st-da.st-bg.st-db.st-dc > svg{
               color: #00ffff !important;                }                

      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(4) > div > div > div > div > div.st-ak.st-al.st-bd.st-be.st-bf.st-as.st-bg.st-bh.st-ar.st-bi.st-bj.st-bk.st-bl > div.st-eg.st-cn.st-ar.st-ca.st-c9.st-eh{
               color: white !important;                }                

      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(4) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > span{
               background-color: rgba(200,200,200,0.3) !important;                }                
                  
                  
      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(5) > div > div > div > div{
               background-color: rgba(0,0,0,0) !important;                }

      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(5) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > div.st-eg.st-dm.st-c9.st-db.st-da.st-eh{
               color: white !important}                

      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(5) > div > div > div > div > div.st-ak.st-al.st-as.st-da.st-bg.st-db.st-dc > svg{
               color: #00ffff !important;                }                

      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(5) > div > div > div > div > div.st-ak.st-al.st-bd.st-be.st-bf.st-as.st-bg.st-bh.st-ar.st-bi.st-bj.st-bk.st-bl > div.st-eg.st-cn.st-ar.st-ca.st-c9.st-eh{
               color: white !important;                }                

      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(5) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > span{
               background-color: rgba(200,200,200,0.3) !important;                }                
                  
                  

      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(6) > div > div > div > div{
               background-color: rgba(0,0,0,0) !important;}

      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(6) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > div.st-eg.st-dm.st-c9.st-db.st-da.st-eh{
               color: white !important}                

      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(6) > div > div > div > div > div.st-ak.st-al.st-as.st-da.st-bg.st-db.st-dc > svg{
               color: #00ffff !important;
                     }                

      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(6) > div > div > div > div > div.st-ak.st-al.st-bd.st-be.st-bf.st-as.st-bg.st-bh.st-ar.st-bi.st-bj.st-bk.st-bl > div.st-eg.st-cn.st-ar.st-ca.st-c9.st-eh{
               color: white !important;
                     }                

   #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(6) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > span{
            background-color: rgba(200,200,200,0.3) !important;
                  }                
                  
                  
   #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(7) > div > div > div > div{
            background-color: rgba(0,0,0,0) !important;
                  }

   #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(7) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > div.st-eg.st-dm.st-c9.st-db.st-da.st-eh{
            color: white !important}                

   #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(7) > div > div > div > div > div.st-ak.st-al.st-as.st-da.st-bg.st-db.st-dc > svg{
            color: #00ffff !important;
                  }                

   #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(7) > div > div > div > div > div.st-ak.st-al.st-bd.st-be.st-bf.st-as.st-bg.st-bh.st-ar.st-bi.st-bj.st-bk.st-bl > div.st-eg.st-cn.st-ar.st-ca.st-c9.st-eh{
            color: white !important;
                  }                

   #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(7) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > span{
            background-color: rgba(200,200,200,0.3) !important;
                  }                
                  
   #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(8) > div > div > div > div{
            background-color: rgba(0,0,0,0) !important;}

   #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(8) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > div.st-eg.st-dm.st-c9.st-db.st-da.st-eh{
            color: white !important}

   #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(8) > div > div > div > div > div.st-ak.st-al.st-as.st-da.st-bg.st-db.st-dc > svg{
            color: #00ffff !important;}                

   #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(8) > div > div > div > div > div.st-ak.st-al.st-bd.st-be.st-bf.st-as.st-bg.st-bh.st-ar.st-bi.st-bj.st-bk.st-bl > div.st-eg.st-cn.st-ar.st-ca.st-c9.st-eh{
            color: white !important;}                

   #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(8) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > span{
            background-color: rgba(200,200,200,0.3) !important;}                
                  

   #root > div:nth-child(1) .st-emotion-cache-ocqkz7 > div:nth-child(1),
   #root > div:nth-child(1) .st-emotion-cache-ocqkz7 > div:nth-child(2),
   #root > div:nth-child(1) .st-emotion-cache-ocqkz7 > div:nth-child(3),
   #root > div:nth-child(1) .st-emotion-cache-ocqkz7 > div:nth-child(4),
   #root > div:nth-child(1) .st-emotion-cache-ocqkz7 > div:nth-child(5) {
      border: 1px solid #00ff00;
      border-radius: 5px;
      padding: 3px;
      text-align: center !important;

   }
                        
                  
   /* Hide specific label */
   #root > div:nth-child(1) .st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(n+1):nth-child(-n+5) > div > div > div > div:nth-child(2) > div > label {
      display: none;
   }

   /* Hide  */
   #root > div:nth-child(1) .st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(n+1):nth-child(-n+5),
   #root > div:nth-child(1) .st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(8) {
      display: none;
   }



   #root > div:nth-child(2) > div > div > div > div > div > div > ul > div{
   background-color: darkgray;
   }

   .metric-title {
            font-size: 14px; /* Cambia el tamaño del título */
            color: #00FF00; /* Cambia el color del título */
            # border: 1px solid white;
        }
               
/* selector años */            
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1itdyc2.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(2) > div{
               display:flex;
               justify-content: flex-end;
               font-size:18px !important;
               }
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1itdyc2.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(3) > div > label > div > div > div > p{
               font-size:16px !important;
}

               /*    titulo del dashboard */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(7) > div > div > nav > a{
    width: 50vw !important;
    font-size: 40px;
    font-family: Arial;
    color: rgb(0, 255, 255);
    margin-left: 2.5rem;
    text-align: end !important;
               }   

               /*  header fijo */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(14){
                position: fixed;
                top: 110px;
               right: 1.3rem !important;
                background-color: none;
                z-index: 1000;
                width: 70vw;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
               }
               

#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5{
 margin: 95px 0 0 0 !important;
                }               

#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5{
         padding-left: 1rem !important;
         padding-right: 1rem !important;
               }
/* sidebar */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1itdyc2.eczjsme18{
background-color: #000000 !important;
               }  

/* card indicator  */                
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(14) > div:nth-child(1) > div > div > div,
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(14) > div:nth-child(2) > div > div > div,
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(14) > div:nth-child(3) > div > div > div,
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(14) > div:nth-child(4) > div > div > div,
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(14) > div:nth-child(5) > div > div > div{
background-color: rgba(0,0,0,.7)
               }               

/* sidebar img   */  
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1itdyc2.eczjsme18{
     background-image: url('https://i.imgur.com/MNid628.jpg');
    position: relative;
    user-select: auto;
    width: 422px;
    height: auto;
    box-sizing: border-box;
    flex-shrink: 0;
    background-repeat: no-repeat;
    background-size: cover;
}                          
             
               
         </style> """, unsafe_allow_html=True)
   

# styles en navbar:   
def style_navbar():
         st.markdown(
         """
         <link href="https://use.fontawesome.com/releases/v5.15.4/css/all.css" rel="stylesheet">
         <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">

         <style>
         .stApp {
            background-color: #1E1E1E;
            color: #00FF00;
         }
         header{
         background-color: rgba(0,0,0,0) !important;
         }
            .navbar-custom {
                  top: 0rem !important; 
                  position: fixed !important;
                  width: calc(100% - 0px) !important;
                  right: 0px !important; 
                  z-index: 1000 !important;
                  background-color: black !important; 
            }
            #navbarNav{
            margin: 2.3rem 2rem 0 0 !important;
                  display: flex;
                  justify-content: flex-end;
            }
         
         </style>
         """,
         unsafe_allow_html=True
      )

# style en cuadros generales:
def style_title()         :
          st.markdown("""<style>.metric-title {
            font-size: 18px;
            color: #00FF00;
            }</style>""", unsafe_allow_html=True)