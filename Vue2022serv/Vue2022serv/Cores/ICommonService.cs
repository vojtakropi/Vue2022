using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Web;

namespace Vue2022serv.Cores
{
    public interface ICommonService
    {

        HttpResponseMessage GetResponse(string content);

    }
}