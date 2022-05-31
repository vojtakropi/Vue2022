using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using Vue2022serv.Cores;

namespace Vue2022serv.Controllers
{
    public class BaseController : ApiController
    {
        public ICommonService commonService;
        public BaseController(ICommonService commonService)
        {
            this.commonService = commonService;
        }

    }
}
