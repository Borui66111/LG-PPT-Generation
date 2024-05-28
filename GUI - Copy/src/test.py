from llm import *
def run(content=None,min_slides=10,word_limit=60):
    chain,content=None,"3 days stopover in Singapore" if not content else content
    chain=chain if chain else create_chain(functions_config={ 'functions': Outline,'function_call': { "name": 'Outline' }},system_message=f'''you are a helpful assistant to create a ppt. There should be at least {min_slides} body slides''')
    resp=chat(content,chain)
    title=resp['slides']

    resp1=chat([f'''topic:{content};title:'''+i for i in title],force_invoke=0,chain=create_chain(model_name='gpt-4o',functions_config={ 'functions': Slide,'function_call': { "name": 'Slide' }},temperature=0,system_message=f'''Fill in the content according to the guide. it must contain illustrations by means of specific examples (who, when, where) and must offer insights into the topic. you must use layman\'s terms to explain complex concepts. you must engage the audience by posing questions or present hypothetical scenarios. make sure the length is no more than {word_limit} words for one slide''',))
    txt=[i['content'] for i in resp1]

    vis=chat(txt,force_invoke=0,chain=create_chain(functions_config={ 'functions': Visual,'function_call': { "name": 'Visual' }},temperature=0,))
    name='../output/test.pptx' # 2 shapes instead of 3
    ppt=Prs.PPT()
    icon_width=1+1/3;text=txt
    for i in range(len(text)):
        slide=ppt.add_slide(slide_layout=5) # only title
        ppt.add_text_chunk(slide.shapes,list(map(lambda x:Prs.Emu(x),[457200, 1600200, 8229600*0.8, 4525963])))
        ppt.change_text(slide.shapes[0],title[i])
        ppt.change_text(slide.shapes[1],text[i])
        ppt.set_font(slide.shapes[1],size=18)
    ppt.prs_save(ppt.prs,name=name)

    # for slide in ppt.prs.slides:
    #     ppt.add_img(slide,img='../output/bg_transparent.png',pos=[0,0],width=ppt.prs.slide_width,height=ppt.prs.slide_height)
    ppt.prs_save(ppt.prs,name=name)
        