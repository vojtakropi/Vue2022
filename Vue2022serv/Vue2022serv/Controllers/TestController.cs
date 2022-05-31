using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;

namespace Vue2022serv.Controllers
{
    public class TestController : ApiController
    {


        [HttpGet]
        [ActionName("all")]
        public string All()
        {
            return "yes";
        }


    }
}
