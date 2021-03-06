# Generated by the windmill services transformer
from windmill.authoring import WindmillTestClient

def setup_module(module):
    module.client = WindmillTestClient(__name__)

def testPass():
    client.click(id=u'story')
    client.type(text=u'asdfaasdf', id=u'story')
    client.click(id=u'flavor')
    client.select(option=u'Strawberry', id=u'flavor')
    client.click(xpath=u"/html/body/form[@id='frmfrm']/select[@id='flavor']/option[2]")
    client.click(xpath=u"/html/body/form[@id='frmfrm']/p/input[1]")
    client.asserts.assertValue(validator=u'', id=u'junkfield')
    
def testFail():
    client.asserts.assertValue(validator=u'', id=u'junkfieldasdf')