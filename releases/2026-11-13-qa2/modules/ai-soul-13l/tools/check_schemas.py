from pathlib import Path
import sys,json,copy

from jsonschema import Draft202012Validator
p=Path(__file__).resolve().parents[1]
m=p/'machine'
s=json.loads((m/'envelope.schema.json').read_text()); cfgs=json.loads((m/'configuration.schema.json').read_text())
Draft202012Validator.check_schema(s);Draft202012Validator.check_schema(cfgs)
v=Draft202012Validator(s);vc=Draft202012Validator(cfgs)
ex=json.loads((m/'example-envelope.json').read_text());cfg=json.loads((m/'default-configuration.json').read_text())
results=[]
def case(name,obj,expected,validator=v):
 errors=sorted(validator.iter_errors(obj),key=lambda e:str(e.path))
 valid=not errors
 results.append({'id':name,'expected_valid':expected,'actual_valid':valid,'passed':valid==expected,'error_count':len(errors)})
case('valid_local_no_retention',ex,True)
case('valid_safe_configuration',cfg,True,vc)
q=copy.deepcopy(ex);q['output']['claims'][0]['status']='PASS';q['output']['claims'][0].pop('criterion');case('pass_without_criterion_rejected',q,False)
q=copy.deepcopy(ex);q['output']['claims'][0]['status']='PASS';q['output']['claims'][0]['source_ref']=None;case('pass_without_source_rejected',q,False)
q=copy.deepcopy(ex);q['persistence']='local_opt_in';case('local_retention_without_consent_rejected',q,False)
q=copy.deepcopy(ex);q['persistence']='external_opt_in';q['consent_record']={k:'example' for k in ['evidence_ref','purpose','scope','retention','withdrawal_route']};q['external_action']={'state':'draft','action':'send','material':'example','purpose':'example','recipient':'example','channel':'example','payload_preview':'example'};case('external_retention_with_draft_only_rejected',q,False)
q=copy.deepcopy(ex);q['external_action']={'state':'executed','action':'send','material':'example','purpose':'example','recipient':'example','channel':'example','payload_preview':'example','authorization_ref':'example'};case('executed_action_without_result_evidence_rejected',q,False)
q=copy.deepcopy(ex);q['module_route']=['unknown'];case('unknown_route_rejected',q,False)
q=copy.deepcopy(ex);q['hidden_telemetry']=True;case('undeclared_envelope_property_rejected',q,False)
q=copy.deepcopy(cfg);q['network']='on';case('configuration_network_on_rejected',q,False,vc)
q=copy.deepcopy(cfg);q['memory']='external_opt_in';case('configuration_external_memory_default_rejected',q,False,vc)
q=copy.deepcopy(ex);q['choice']='accept';case('resolved_choice_without_evidence_rejected',q,False)
q=copy.deepcopy(cfg);q['selected_modules']=['NITYA'];case('missing_dependency_closure_rejected',q,False,vc)
q=copy.deepcopy(ex);q['external_action']={'state':'executed','action':'send','material':'example','purpose':'example','recipient':'example','channel':'example','payload_preview':'example','authorization_ref':'example','result_evidence_ref':'example','retention':'none','withdrawal_route':'example'};case('executed_transfer_without_consent_record_rejected',q,False)
q=copy.deepcopy(ex);q['choice']='pause';q['choice_record']={'actor_class':'human','evidence_ref':'user-message-example'};case('recorded_human_pause_valid',q,True)
result={'schema':'suti.artifact-verification.v1','scope':'JSON Schema draft 2020-12 validity and positive/negative data vectors only','date':'2026-11-13','validator':'jsonschema.Draft202012Validator (isolated temporary installation)','state':'PASS' if all(x['passed'] for x in results) else 'FAIL','results':results,'limits':['No host enforcement, model behavior, native language review, security testing or deployment is implied.']}

print(result['state'],len(results),'schema vectors')
if result['state']!='PASS':raise SystemExit(1)
