from django import forms
from .models import analises, ccotacao





class AnaliseForm(forms.ModelForm):
    class Meta:
        model = analises
        fields = ['numero_cotacao', 'pn', 'rev', 'cliente', 'contato', 'materia_prima', 'data', 'quantidade', 'assinatura', 'risco_nt', 'detalhe_risco_nt',
                  'risco_pe','detalhe_risco_pe', 'risco_fin', 'detalhe_risco_fin', 'rec_disp', 'detalhe_rec_disp','tolerancia','detalhe_tol', 
                  'risco_trat', 'anot_risco', 'detalhe_anot_risco', 'not_aplicable', 
                  'decline', 'cliente_avis','cert_qualidade', 'not_qualify', 'embalagem','client_process', 'terc_proce', 'not_recurring','use_device',
                  'obs']
        
        labels = {
                'numero_cotacao': 'Número da Cotação(Quote Number)',
                'pn': 'PN',
                'contato': 'Contato(Contact)', 'cliente': 'Cliente(Client)', 'materia_prima': 'Matéria Prima(Raw Material)','data': 'Data(Date)', 
                'quantidade': 'Quantidade(Quantity)', 'assinatura': 'Código de Assinatura(Assinature Code)', 'risco_nt': 'Risco de Novas Tecnologias (New Technologies Risk)', 
                'detalhe_risco_nt': 'Detalhar(Detail)',
                  'risco_pe': 'Risco de Prazo de Entrega (Delivery Time Risk)','detalhe_risco_pe': 'Detalhar(Detail)', 'risco_fin': 'Risco Financeiro (Financial Risk)', 
                  'detalhe_risco_fin': 'Detalhar(Detail)', 'rec_disp': 'Existem recursos disponíveis (máquinas, ferramentas) para fabricação do item?(Are there resources available (machines, tools) to manufacture the item?)', 
                  'detalhe_rec_disp': 'Detalhar(Detail)','tolerancia': 'Tolerâncias especificadas podem ser verificadas com os meios de medição disponíveis?(Can specified tolerances be checked with the available measuring instruments?)',
                  'detalhe_tol': 'Detalhar(Detail)', 
                  'risco_trat': 'Risco de Tratamento Térmico e/ou Superficial? (Risk of Heat and / or Surface Treatment?)', 'detalhe_risco_trat': 'Detalhar(Detail)', 
                  'anot_risco': 'Outros riscos (Other risks)', 'detalhe_anot_risco': 'Detalhar(Detail)', 'not_aplicable': 'Não aplicável (Not applicable)', 
                  'decline': 'Declinar(Decline)', 'cliente_avis': 'Avisado cliente?(Customer Warned?)',
                  'cert_qualidade': 'Requisitos de Certificação da Qualidade conforme requerido? (Quality certification requirements as required?) ', 
                  'not_qualify': 'Existem requisitos ligados à normas e processos especiais não qualificados?(Are there requirements related to special unqualified standards and processes?)', 
                  'embalagem': 'Existem requisitos específicos de embalagem? (Are there specific packaging requirements?)',
                  'client_process': 'Necessária alteração do processo do cliente? (Need to change the customers process?)', 
                  'terc_proce':'Existem processos de terceiros? (Are there any Sub-tier Supplier processes?)', 'not_recurring': 'Não recorrente? (Not recurring?)',
                  'use_device': 'Utiliza Dispositivo? (Use Device?)'
        }
        
      
        
       
###class CotacaoForm(forms.ModelForm):
  ###class Meta:
    ###model = ccotacao
    ####fields = ['numero_cotacao', 'pn', 'rev', 'cliente', 'contato', 'materia_prima', 'data', 'quantidade', 'assinatura', '']