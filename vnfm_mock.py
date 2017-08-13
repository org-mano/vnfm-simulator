from flask import Flask, request, jsonify
from flask.ext.restful import Resource, Api
import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%H:%M:%S',
                filename='/var/log/vnfm_mock.log',
                filemode='a')

app = Flask(__name__)
api = Api(app)

myarray = []


class Vnfs(Resource):
    def post(self):
        logging.info('begin InstantiateVnf ...')
        param = {
            'vnfoid': request.form['vnfoid'],
            'vnfmid': request.form['vnfmid'],
            'vnfd': request.form['vnfd'],
            'vnfurl': request.form['vnfurl'],
            #'extention': request.form[]
        }
        logging.info(param)
        logging.info('end init vnf')

        resp = {
            'vnfistanceid': '1234',
            'jobid': '11111'
        }
        logging.info('begin response')
        logging.info(resp)
        return resp

    def get(self):
        logging.info('query all vnf')
        allvnf = []
        one = {'vnfinstanceid':'1', 'vnfinstancestatus':'1'}
        allvnf.append(one)
        resp = {'vnflist': allvnf}
        logging.info(resp)
        return resp


class Vnfs_one(Resource):
    def get(self, vnfid):
        #return "all vnf"
        logging.info('query one Vnf, vnfid= ' + vnfid)
        resp = {
            'vnfinstancestatus': '1'
        }
        logging.info(resp)
        return resp

    def delete(self, vnfid):
        logging.info('delete vnf, vnfid= ' + vnfid)
        resp = {'jobid':'123'}
        logging.info(resp)
        return resp

class Vnfs_scale(Resource):
    def put(self, vnfid):
        logging.info('vnfs scale, vnfid= ' + vnfid)
        param = {
            'nfvoid': request.form['nfvoid'],
            'vnfmid': request.form['vnfmid'],
            'scaletype': request.form['scaletype'],
        }
        logging.info(param)
        logging.info('end scale vnf')
 
        resp = {
            'jobid': '1234'
        }
        logging.info(resp)
        return resp

class Vnfs_update(Resource):
    def put(self, vnfid):
        logging.info('vnfs update, vnfid= ' + vnfid)
        param = {
            'nfvoid': request.form['nfvoid'],
            'vnfmid': request.form['vnfmid'],
            'VNFInstanceID': request.form['VNFInstanceID'],
            'VNFSoftwareVersion': request.form['VNFSoftwareVersion'],
            'vnfd': request.form['vnfd'],
            'VNFGOSImageURL': request.form['VNFGOSImageURL'],
            'VNFSoftwareURL': request.form['VNFSoftwareURL'],
        }
        logging.info(param)
        logging.info('end update vnf')
 
        resp = {
            'jobid': '1234'
        }
        logging.info(resp)
        return resp

class Jobs(Resource):
    def get(self, jobid):
        logging.info('query job, jobid=' + jobid)
        allHis = []
        one = {'progress':'40', 'status':'processing'}
        allHis.append(one)
        respDesc = {'progress':'40', 'responseHistoryList': allHis}
        resp = {'jobId': jobid, 'responseDescriptor':respDesc}
        logging.info(resp)
        return resp

class Policies(Resource):
    def post(self, vnfid):
        logging.info('post policy, vnfid=' + vnfid)
        param = {
            'nfvoid': request.form['nfvoid'],
            'vnfmid': request.form['vnfmid'],
            'policyId': request.form['policyId'],
            'policy': request.form['policy'],
        }
        logging.info(param)
        
        resp = {
            'policyid': '6'
        }
        logging.info(resp)
        return resp
    def get(self, vnfid):
        logging.info('get one, vnfid=' + vnfid)
        allPolicies = []
        one = {'policyid':'1', 'policy':'<root/>',  'status':'1'}
        two = {'policyid':'2', 'policy':'<root/>',  'status':'1'}
        allPolicies.append(one)
        allPolicies.append(two)
        resp = {'policylist': allPolicies}
        logging.info(resp)
        return resp


class Policies_update(Resource):
    def put(self, vnfid, policyid):
        logging.info('put policy, vnfid=' + vnfid + ' policyid=' + policyid)
        param = {
            'nfvoid': request.form['nfvoid'],
            'vnfmid': request.form['vnfmid'],
            'policy': request.form['policy'],
        }
        logging.info(param)
        return 'ok'

    def delete(self, vnfid, policyid):
        logging.info('delete policy, vnfid=' + vnfid + ' policyid=' + policyid)
        return 'delete ok'
    def get(self, vnfid, policyid):

        logging.info('get policy, vnfid=' + vnfid + ' policyid=' + policyid)
        resp = {
            'policy': '<root/>',
            'status': '1',
        }
        logging.info(resp)
        return resp

class Policies_active_all(Resource):
    def put(self, vnfid):
        param = {
            'nfvoid': request.form['nfvoid'],
            'vnfmid': request.form['vnfmid'],
        }
        logging.info(param)
        #resp = {
        #    'nfvoid': '12345678',
        #    'vnfmid': '123',
        #}
        #logging.info(resp)
        #return resp
        return 'ok'
        
class Policies_active_one(Resource):
    def put(self, vnfid, policyid):
        param = {
            'nfvoid': request.form['nfvoid'],
            'vnfmid': request.form['vnfmid'],
        }
        logging.info(param)
        return 'ok'

class Policies_deactive_all(Resource):
    def put(self, vnfid):
        param = {
            'nfvoid': request.form['nfvoid'],
            'vnfmid': request.form['vnfmid'],
        }
        logging.info(param)
        return 'ok'

class Policies_deactive_one(Resource):
    def put(self, vnfid, policyid):
        param = {
            'nfvoid': request.form['nfvoid'],
            'vnfmid': request.form['vnfmid'],
        }
        logging.info(param)
        return 'ok'

api.add_resource(Vnfs, '/v1/vnfs')
api.add_resource(Vnfs_one, '/v1/vnfs/<string:vnfid>')
api.add_resource(Vnfs_scale, '/v1/vnfs/<string:vnfid>/scale')
api.add_resource(Vnfs_update, '/v1/vnfs/<string:vnfid>/update')
api.add_resource(Jobs, '/v1/jobs/<string:jobid>')

api.add_resource(Policies, '/v1/vnfs/<string:vnfid>/policies')
api.add_resource(Policies_update, '/v1/vnfs/<string:vnfid>/policies/<string:policyid>')
api.add_resource(Policies_active_all, '/v1/vnfs/<string:vnfid>/policies/active')
api.add_resource(Policies_active_one, '/v1/vnfs/<string:vnfid>/policies/<string:policyid>/active')
api.add_resource(Policies_deactive_all, '/v1/vnfs/<string:vnfid>/policies/deactive')
api.add_resource(Policies_deactive_one, '/v1/vnfs/<string:vnfid>/policies/<string:policyid>/deactive')


if __name__ == '__main__':
    app.run(debug=True,
        host='0.0.0.0',
        port=5000
    )

