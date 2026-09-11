import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
const read=p=>fs.readFileSync(new URL('../'+p,import.meta.url),'utf8');
test('Salesforce project targets explicit API and keeps original acceptance rows',()=>{const p=JSON.parse(read('sfdx-project.json'));assert.equal(p.sourceApiVersion,'64.0');const m=JSON.parse(read('module.json'));assert.equal(m.platform,'Salesforce');assert.equal(m.requirements.length,5);assert.ok(m.requirements.every(r=>r.acceptance&&r.blocker));});
test('every native test and invocable source is paired with deployable metadata',()=>{const m=JSON.parse(read('module.json'));for(const name of m.native_tests){assert.match(read(`force-app/main/default/classes/${name}.cls`),/@IsTest/i);assert.match(read(`force-app/main/default/classes/${name}.cls-meta.xml`),/<apiVersion>64.0/);const source=read(`force-app/main/default/classes/${name.replace(/Test$/,'')}.cls`);assert.match(source,/public with sharing class/);assert.match(source,/@InvocableMethod/);assert.doesNotMatch(source,/HttpRequest|HttpResponse|Messaging\./);}});
test('release limits remain explicit',()=>{assert.match(read('README.md'),/have \*\*not\*\* run/);assert.match(read('SOURCES.md'),/developer.salesforce.com/);});
