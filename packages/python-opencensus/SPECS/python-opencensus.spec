%global srcname opencensus
%global _description %{expand:OpenCensus provides a framework to measure a server's resource usage and collect
performance stats. This package contains Python related utilities and supporting
software needed by OpenCensus.}

Name:           python-%{srcname}
Version:        0.7.9
Release:        1%{?dist}
Summary:        A stats collection and distributed tracing framework

License:        ASL 2.0
URL:            https://github.com/census-instrumentation/%{srcname}-python
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Use unittest instead of unittest2 for tests
Patch0:         %{name}-0.7.7-unittest2.patch
# Fix dependency names/versions in setup.py files to match those provided by
# Fedora
Patch1:         %{name}-0.7.7-requirements.patch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
# Required for tests
BuildRequires:  %{py3_dist bitarray}
BuildRequires:  %{py3_dist django}
BuildRequires:  %{py3_dist flask}
BuildRequires:  %{py3_dist gevent}
BuildRequires:  %{py3_dist google-api-core}
BuildRequires:  %{py3_dist googleapis-common-protos}
BuildRequires:  %{py3_dist grpcio}
BuildRequires:  %{py3_dist mock}
BuildRequires:  %{py3_dist mysql-connector-python}
BuildRequires:  %{py3_dist opencensus-proto}
BuildRequires:  %{py3_dist prometheus-client}
BuildRequires:  %{py3_dist psutil}
BuildRequires:  %{py3_dist psycopg2}
BuildRequires:  %{py3_dist pymongo}
BuildRequires:  %{py3_dist pymysql}
BuildRequires:  %{py3_dist pyramid}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist requests}
BuildRequires:  %{py3_dist retrying}
BuildRequires:  %{py3_dist sqlalchemy}
BuildRequires:  %{py3_dist thrift}
BuildRequires:  %{py3_dist wrapt}
# Required for documentation
BuildRequires:  %{py3_dist sphinx}
BuildArch:      noarch

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}


%package -n python3-%{srcname}-context
Summary:        OpenCensus Runtime Context
%{?python_provide:%python_provide python3-%{srcname}-context}

%description -n python3-%{srcname}-context
The OpenCensus Runtime Context provides in-process context propagation.


%package -n python3-%{srcname}-correlation
Summary:        W3C Correlation Context
%{?python_provide:%python_provide python3-%{srcname}-correlation}

%description -n python3-%{srcname}-correlation
%{summary}.


%package -n python3-%{srcname}-ext-azure
Summary:        OpenCensus Azure Monitor Exporters
%{?python_provide:%python_provide python3-%{srcname}-ext-azure}

%description -n python3-%{srcname}-ext-azure
%{summary}.


%package -n python3-%{srcname}-ext-datadog
Summary:        OpenCensus Datadog Exporter
%{?python_provide:%python_provide python3-%{srcname}-ext-datadog}

%description -n python3-%{srcname}-ext-datadog
%{summary}.


%package -n python3-%{srcname}-ext-dbapi
Summary:        OpenCensus Database API Integration
%{?python_provide:%python_provide python3-%{srcname}-ext-dbapi}

%description -n python3-%{srcname}-ext-dbapi
%{summary}.


%package -n python3-%{srcname}-ext-django
Summary:        OpenCensus Django Integration
%{?python_provide:%python_provide python3-%{srcname}-ext-django}

%description -n python3-%{srcname}-ext-django
%{summary}.


%package -n python3-%{srcname}-ext-flask
Summary:        OpenCensus Flask Integration
%{?python_provide:%python_provide python3-%{srcname}-ext-flask}

%description -n python3-%{srcname}-ext-flask
%{summary}.


%package -n python3-%{srcname}-ext-gevent
Summary:        OpenCensus gevent helper
%{?python_provide:%python_provide python3-%{srcname}-ext-gevent}

%description -n python3-%{srcname}-ext-gevent
%{summary}.


# %%package -n python3-%%{srcname}-ext-google-cloud-clientlibs
# Summary:        OpenCensus Google Cloud Client Libraries Integration
# %%{?python_provide:%%python_provide python3-%%{srcname}-ext-google-cloud-clientlibs}

# %%description -n python3-%%{srcname}-ext-google-cloud-clientlibs
# %%{summary}.


%package -n python3-%{srcname}-ext-grpc
Summary:        OpenCensus gRPC Integration
%{?python_provide:%python_provide python3-%{srcname}-ext-grpc}

%description -n python3-%{srcname}-ext-grpc
%{summary}.


%package -n python3-%{srcname}-ext-httplib
Summary:        OpenCensus httplib Integration
%{?python_provide:%python_provide python3-%{srcname}-ext-httplib}

%description -n python3-%{srcname}-ext-httplib
%{summary}.


%package -n python3-%{srcname}-ext-jaeger
Summary:        OpenCensus Jaeger Exporter
%{?python_provide:%python_provide python3-%{srcname}-ext-jaeger}

%description -n python3-%{srcname}-ext-jaeger
%{summary}.


%package -n python3-%{srcname}-ext-logging
Summary:        OpenCensus logging Integration
%{?python_provide:%python_provide python3-%{srcname}-ext-logging}

%description -n python3-%{srcname}-ext-logging
%{summary}.


%package -n python3-%{srcname}-ext-mysql
Summary:        OpenCensus MySQL Integration
%{?python_provide:%python_provide python3-%{srcname}-ext-mysql}

%description -n python3-%{srcname}-ext-mysql
%{summary}.


%package -n python3-%{srcname}-ext-ocagent
Summary:        OpenCensus OC-Agent Exporter
%{?python_provide:%python_provide python3-%{srcname}-ext-ocagent}

%description -n python3-%{srcname}-ext-ocagent
%{summary}.


%package -n python3-%{srcname}-ext-postgresql
Summary:        OpenCensus PostgreSQL Integration
%{?python_provide:%python_provide python3-%{srcname}-ext-postgresql}

%description -n python3-%{srcname}-ext-postgresql
%{summary}.


%package -n python3-%{srcname}-ext-prometheus
Summary:        OpenCensus Prometheus Exporter
%{?python_provide:%python_provide python3-%{srcname}-ext-prometheus}

%description -n python3-%{srcname}-ext-prometheus
%{summary}.


%package -n python3-%{srcname}-ext-pymongo
Summary:        OpenCensus pymongo Integration
%{?python_provide:%python_provide python3-%{srcname}-ext-pymongo}

%description -n python3-%{srcname}-ext-pymongo
%{summary}.


%package -n python3-%{srcname}-ext-pymysql
Summary:        OpenCensus PyMySQL Integration
%{?python_provide:%python_provide python3-%{srcname}-ext-pymysql}

%description -n python3-%{srcname}-ext-pymysql
%{summary}.


%package -n python3-%{srcname}-ext-pyramid
Summary:        OpenCensus Pyramid Integration
%{?python_provide:%python_provide python3-%{srcname}-ext-pyramid}

%description -n python3-%{srcname}-ext-pyramid
%{summary}.


%package -n python3-%{srcname}-ext-requests
Summary:        OpenCensus requests Integration
%{?python_provide:%python_provide python3-%{srcname}-ext-requests}

%description -n python3-%{srcname}-ext-requests
%{summary}.


%package -n python3-%{srcname}-ext-sqlalchemy
Summary:        OpenCensus SQLAlchemy Integration
%{?python_provide:%python_provide python3-%{srcname}-ext-sqlalchemy}

%description -n python3-%{srcname}-ext-sqlalchemy
%{summary}.


# %%package -n python3-%%{srcname}-ext-stackdriver
# Summary:        OpenCensus Stackdriver Trace Exporter
# %%{?python_provide:%%python_provide python3-%%{srcname}-ext-stackdriver}

# %%description -n python3-%%{srcname}-ext-stackdriver
# %%{summary}.


%package -n python3-%{srcname}-ext-threading
Summary:        OpenCensus threading Integration
%{?python_provide:%python_provide python3-%{srcname}-ext-threading}

%description -n python3-%{srcname}-ext-threading
%{summary}.


%package -n python3-%{srcname}-ext-zipkin
Summary:        OpenCensus Zipkin Exporter
%{?python_provide:%python_provide python3-%{srcname}-ext-zipkin}

%description -n python3-%{srcname}-ext-zipkin
%{summary}.


%package doc
Summary:        Documentation for %{name}

%description doc
This package provides documentation for %{name}.


%prep
%autosetup -p0 -n %{srcname}-python-%{version}

# Remove bundled egg-info
for i in $(find . -name "setup.py"); do
    rm -rf ${i%/*}/*.egg-info
done

# Delete extensions which can't be installed because of missing dependencies in
# Fedora
rm -r \
    contrib/opencensus-ext-google-cloud-clientlibs/ \
    contrib/opencensus-ext-stackdriver/
rm -r tests/system/stats/stackdriver/


%build
for i in $(find . -name "setup.py"); do
    pushd ${i%/*}
    %py3_build
    popd
done

# Build documentation
PYTHONPATH=
for i in $(find $PWD -name "setup.py"); do
    PYTHONPATH+="${i%/*}:"
done
export PYTHONPATH=${PYTHONPATH%:}
%make_build html
rm docs/build/html/.buildinfo


%install
for i in $(find . -name "setup.py"); do
    pushd ${i%/*}
    %py3_install
    popd
done


%check
PYTHONPATH=$RPM_BUILD_ROOT/%{python3_sitelib}/ pytest-%{python3_version} tests/unit/ context/ contrib/


%files -n python3-%{srcname}
%doc CHANGELOG.md CONTRIBUTING.md README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}/
%exclude %{python3_sitelib}/%{srcname}/common/correlationcontext/
%exclude %{python3_sitelib}/%{srcname}/common/runtime_context/
%exclude %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}-*.egg-info/


%files -n python3-%{srcname}-context
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/common/
%{python3_sitelib}/%{srcname}/common/runtime_context/
%{python3_sitelib}/%{srcname}_context-*.egg-info/


%files -n python3-%{srcname}-correlation
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/common/
%{python3_sitelib}/%{srcname}/common/correlationcontext/
%{python3_sitelib}/%{srcname}_correlation-*.egg-info/


%files -n python3-%{srcname}-ext-azure
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/azure/
%{python3_sitelib}/%{srcname}_ext_azure-*.egg-info/


%files -n python3-%{srcname}-ext-datadog
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/datadog/
%{python3_sitelib}/%{srcname}_ext_datadog-*.egg-info/


%files -n python3-%{srcname}-ext-dbapi
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/dbapi/
%{python3_sitelib}/%{srcname}_ext_dbapi-*.egg-info/


%files -n python3-%{srcname}-ext-django
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/django/
%{python3_sitelib}/%{srcname}_ext_django-*.egg-info/


%files -n python3-%{srcname}-ext-flask
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/flask/
%{python3_sitelib}/%{srcname}_ext_flask-*.egg-info/


%files -n python3-%{srcname}-ext-gevent
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/gevent/
%{python3_sitelib}/%{srcname}_ext_gevent-*.egg-info/


# %%files -n python3-%%{srcname}-ext-google-cloud-clientlibs
# %%doc context/opencensus-context/{CHANGELOG.md,README.rst}
# %%license LICENSE
# %%dir %%{python3_sitelib}/%%{srcname}/ext/
# %%{python3_sitelib}/%%{srcname}/ext/google_cloud_clientlibs/
# %%{python3_sitelib}/%%{srcname}_ext_google_cloud_clientlibs-*.egg-info/


%files -n python3-%{srcname}-ext-grpc
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/grpc/
%{python3_sitelib}/%{srcname}_ext_grpc-*.egg-info/


%files -n python3-%{srcname}-ext-httplib
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/httplib/
%{python3_sitelib}/%{srcname}_ext_httplib-*.egg-info/


%files -n python3-%{srcname}-ext-jaeger
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/jaeger/
%{python3_sitelib}/%{srcname}_ext_jaeger-*.egg-info/


%files -n python3-%{srcname}-ext-logging
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/logging/
%{python3_sitelib}/%{srcname}_ext_logging-*.egg-info/


%files -n python3-%{srcname}-ext-mysql
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/mysql/
%{python3_sitelib}/%{srcname}_ext_mysql-*.egg-info/


%files -n python3-%{srcname}-ext-ocagent
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/ocagent/
%{python3_sitelib}/%{srcname}_ext_ocagent-*.egg-info/


%files -n python3-%{srcname}-ext-postgresql
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/postgresql/
%{python3_sitelib}/%{srcname}_ext_postgresql-*.egg-info/


%files -n python3-%{srcname}-ext-prometheus
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/prometheus/
%{python3_sitelib}/%{srcname}_ext_prometheus-*.egg-info/


%files -n python3-%{srcname}-ext-pymongo
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/pymongo/
%{python3_sitelib}/%{srcname}_ext_pymongo-*.egg-info/


%files -n python3-%{srcname}-ext-pymysql
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/pymysql/
%{python3_sitelib}/%{srcname}_ext_pymysql-*.egg-info/


%files -n python3-%{srcname}-ext-pyramid
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/pyramid/
%{python3_sitelib}/%{srcname}_ext_pyramid-*.egg-info/


%files -n python3-%{srcname}-ext-requests
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/requests/
%{python3_sitelib}/%{srcname}_ext_requests-*.egg-info/


%files -n python3-%{srcname}-ext-sqlalchemy
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/sqlalchemy/
%{python3_sitelib}/%{srcname}_ext_sqlalchemy-*.egg-info/


# %%files -n python3-%%{srcname}-ext-stackdriver
# %%doc context/opencensus-context/{CHANGELOG.md,README.rst}
# %%license LICENSE
# %%dir %%{python3_sitelib}/%%{srcname}/ext/
# %%{python3_sitelib}/%%{srcname}/ext/stackdriver/
# %%{python3_sitelib}/%%{srcname}_ext_stackdriver-*.egg-info/


%files -n python3-%{srcname}-ext-threading
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/threading/
%{python3_sitelib}/%{srcname}_ext_threading-*.egg-info/


%files -n python3-%{srcname}-ext-zipkin
%doc context/opencensus-context/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/zipkin/
%{python3_sitelib}/%{srcname}_ext_zipkin-*.egg-info/


%files doc
%doc docs/build/html/
%license LICENSE


%changelog
* Sat Jun 27 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.7.9-1
- Update to 0.7.9

* Mon Jun 15 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.7.7-1
- Initial RPM release
