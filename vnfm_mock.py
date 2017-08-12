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

api.add_resource(Vnfs, '/v1/vnfs')
api.add_resource(Vnfs_one, '/v1/vnfs/<string:vnfid>')
api.add_resource(Vnfs_scale, '/v1/vnfs/<string:vnfid>/scale')
api.add_resource(Vnfs_update, '/v1/vnfs/<string:vnfid>/update')
api.add_resource(Jobs, '/v1/jobs/<string:jobid>')

if __name__ == '__main__':
    app.run(debug=True,
        host='0.0.0.0',
        port=5000
    )

