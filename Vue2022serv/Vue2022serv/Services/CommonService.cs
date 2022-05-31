using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Web;
using Vue2022serv.Cores;

namespace Vue2022serv.Services
{
    public class CommonService : ICommonService
    {
        public HttpResponseMessage GetResponse(string content)
        {
            var result = new HttpResponseMessage()
            {
                Content = new StringContent(content)
            };
            result.Content.Headers.ContentType = new System.Net.Http.Headers.MediaTypeHeaderValue("application/json");
            return result;
        }
    }
}