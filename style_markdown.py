import streamlit as st

def style_gen():
   st.markdown("""<style>
               
/* title de indicator */              
   #root > div:nth-child(1) .st-emotion-cache-ocqkz7 > div:nth-child(1),
   #root > div:nth-child(1) .st-emotion-cache-ocqkz7 > div:nth-child(2),
   #root > div:nth-child(1) .st-emotion-cache-ocqkz7 > div:nth-child(3),
   #root > div:nth-child(1) .st-emotion-cache-ocqkz7 > div:nth-child(4),
   #root > div:nth-child(1) .st-emotion-cache-ocqkz7 > div:nth-child(5),
   #root > div:nth-child(1) .st-emotion-cache-ocqkz7 > div:nth-child(6){
      border: 1px solid #00ff00;
      border-radius: 5px;
      padding: 3px;
      text-align: center !important;
      font-size:10px !important;
   }

/* INDICATOR */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5{
         padding:16px 12px;
               }

/* sidebar */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1itdyc2.eczjsme18{
background-color: #000000 !important;
               }  

/* card indicator backgroung-color */                
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(1) > div > div,
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2) > div > div,
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(3) > div > div,
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(4) > div > div,
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(5) > div > div{
background-color: #000000;

               }
/* beetwend title & marker */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(1) > div > div > div,
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2) > div > div > div,
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(3) > div > div > div,
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(4) > div > div > div,
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(5) > div > div > div{
gap:0}               

/* del labels marcator */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(1) > div > div > div > div:nth-child(2) > div > label,
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2) > div > div > div > div:nth-child(2) > div > label,
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(3) > div > div > div > div:nth-child(2) > div > label,
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(4) > div > div > div > div:nth-child(2) > div > label,
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(5) > div > div > div > div:nth-child(2) > div > label{
   display: none !important;
                              }

#sales-sellers,#brands-products,#regions-states,#sales-evolution{
text-align:center}        

/* icon nav streamlit */      
#root > div:nth-child(1) > div.withScreencast > div > div > header > div.st-emotion-cache-15ecox0.ezrtsby0 > div > div:nth-child(1) > button > div > span,               
#root > div:nth-child(1) > div.withScreencast > div > div > header > div.st-emotion-cache-15ecox0.ezrtsby0 > div > div:nth-child(2) > button > div > div,               
#root > div:nth-child(1) > div.withScreencast > div > div > header > div.st-emotion-cache-15ecox0.ezrtsby0 > div > div:nth-child(3) > button > div > div{
               display: none!important}

/* marco de graf sales in the time  */  
#tabs-bui139-tabpanel-1 > div > div > div > div > div > div > div > div > svg:nth-child(1){
      border: 1px solid #00ff00;
      border-radius: 5px;
      padding: 3px;
      text-align: center !important;
      font-size:10px !important;
}
               
/* marco de graf sales in the time  */  
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(21) > div > div > div > div > svg:nth-child(1){
      border: 1px solid #00ff00;
      border-radius: 5px;
      padding: 3px;
      text-align: center !important;
      font-size:10px !important;
               } 

/* hide in sidebar top years  */               
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1itdyc2.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(1){
display: none}                               
               
       

/* style in the selected top  */   
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1itdyc2.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(9) > div > div{
    background-color: rgba(0, 0, 0, .5);
    padding: 4px 0;
    border-radius: 5px;               
}                          

/* backgroun black in the sidebar */               
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-17mvl7w.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11{
    background-image: url('https://i.imgur.com/ZhBoH7H.jpeg')!important;
    background-color: rgba(50,50,50,.7) !important
               }

/* sidebar img   */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-17mvl7w.eczjsme18,               
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1itdyc2.eczjsme18{
    background-image: url('https://i.imgur.com/ZhBoH7H.jpeg')!important;
    background-color: black !important;
    position: relative;
    user-select: auto;
    width: 422px;
    height: auto;
    box-sizing: border-box;
    flex-shrink: 0;
    background-repeat: no-repeat;
}                
/* titles of sections  */
#sales-sellers,
#regions-states{
               margin: 0;
               padding:0
}
/* depliegue del sidebar */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1itdyc2.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1mi2ry5.eczjsme9{
padding: 2px 0}                            

                          
               </style> """, unsafe_allow_html=True)

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
                  width: calc(100%) !important;
                  right: 0px !important; 
                  z-index: 1000 !important;
                  background-color: black !important; 
            }
            #navbarNav{
                  top: 2rem !important; 
                  position: fixed !important;
                  width: calc(100% - 0px) !important;
                  left: 3rem !important; 
                  z-index: 100 !important;
            }
         
         </style>
         """,
         unsafe_allow_html=True
      )
