using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using Vue2022serv.Cores;

namespace Vue2022serv.Controllers
{
    public class ResultsController : BaseController
    {
        private IResultsService resultsService;
        
        public ResultsController(ICommonService commonService, IResultsService resultsService) : base(commonService)
        {
            this.resultsService = resultsService;
        }

        [HttpGet]
        [ActionName("all")]
        public HttpResponseMessage Getall()
        {
            var result = resultsService.Getall();
            var json = JsonConvert.SerializeObject(result, new JsonSerializerSettings()
            {
                ReferenceLoopHandling = ReferenceLoopHandling.Ignore
            });
            return commonService.GetResponse(json);
        }
               
    }
}
