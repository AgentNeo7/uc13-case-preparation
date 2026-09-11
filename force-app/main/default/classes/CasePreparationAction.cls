public with sharing class CasePreparationAction {
 public class Request { @InvocableVariable(required=true) public Id caseId; }
 public class Result { @InvocableVariable public Id caseId; @InvocableVariable public String state; @InvocableVariable public String missing; @InvocableVariable public String sourceReference; @InvocableVariable public Datetime sourceModified; }
 @InvocableMethod(label='Prepare Case Evidence' description='Checks scoped Case fields; does not infer document completeness.')
 public static List<Result> prepare(List<Request> requests) {
  Set<Id> ids=new Set<Id>(); for(Request r:requests) if(r!=null && r.caseId!=null) ids.add(r.caseId);
  Map<Id,Case> rows=new Map<Id,Case>([SELECT Id,Subject,Description,ContactId,LastModifiedDate FROM Case WHERE Id IN :ids WITH USER_MODE]);
  List<Result> out=new List<Result>(); for(Request r:requests) {Result v=new Result(); v.caseId=r==null?null:r.caseId; Case c=rows.get(v.caseId); v.state='UNKNOWN'; v.missing='Case unavailable';
   if(c!=null) {v.missing=''; if(String.isBlank(c.Subject)) v.missing+='Subject;'; if(String.isBlank(c.Description)) v.missing+='Description;'; if(c.ContactId==null) v.missing+='Contact;'; v.state=v.missing==''?'SCOPED_FIELDS_PRESENT':'INCOMPLETE'; v.sourceModified=c.LastModifiedDate; v.sourceReference='/lightning/r/Case/'+c.Id+'/view';} out.add(v);
  } return out;
 }
}
