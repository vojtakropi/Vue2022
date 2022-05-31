using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using Vue2022serv.Cores;

namespace Vue2022serv.Controllers
{
    public class UsersController : BaseController
    {
        private IUsersService usersService;

        public UsersController(ICommonService commonService, IUsersService usersService) : base(commonService)
        {
            this.usersService = usersService;
        }

        IDictionary<string, string> Names = new Dictionary<string, string>();


        [HttpGet]
        [ActionName("login")]
        public string get(string name, string passwd)
        {
            var a = "aaaaa";
            var json = JsonConvert.SerializeObject(a);
            return json;
        }
    }

}
