%global upstream_name lrparsing

%if ! (0%{?fedora} || 0%{?rhel} > 7)
%bcond_without python2
%else
%bcond_with python2
%endif

Name:           python-%{upstream_name}
Version:        1.0.16
Release:        5%{?dist}
Summary:        Python library for constructing LR(1) parsers
License:        AGPLv3+
URL:            http://lrparsing.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Lrparsing is yet another parser for Python. The things that make lrparsing
different is it combines a LR(1) parser with an easy to use grammar written
using Python expressions, a tokeniser, and comes with extensive (and free!)
documentation.

%if %{with python2}
%package -n python2-%{upstream_name}
Summary:        Python 2 library for constructing LR(1) parsers
%{?python_provide:%python_provide python2-%{upstream_name}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

%description -n python2-%{upstream_name}
Lrparsing is yet another parser for Python. The things that make lrparsing
different is it combines a LR(1) parser with an easy to use grammar written
using Python expressions, a tokeniser, and comes with extensive (and free!)
documentation.
%endif

%package -n python%{python3_pkgversion}-%{upstream_name}
Summary:        Python %{python3_version} library for constructing LR(1) parsers
%{?python_provide:%python_provide python%{python3_pkgversion}-%{upstream_name}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{upstream_name}
Lrparsing is yet another parser for Python. The things that make lrparsing
different is it combines a LR(1) parser with an easy to use grammar written
using Python expressions, a tokeniser, and comes with extensive (and free!)
documentation.

%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{upstream_name}
Summary:        Python %{python3_other_version} library for constructing LR(1) parsers
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{upstream_name}}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools

%description -n python%{python3_other_pkgversion}-%{upstream_name}
Lrparsing is yet another parser for Python. The things that make lrparsing
different is it combines a LR(1) parser with an easy to use grammar written
using Python expressions, a tokeniser, and comes with extensive (and free!)
documentation.
%endif

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%if %{with python2}
%py2_build
%endif
%py3_build
%if 0%{?with_python3_other}
%py3_other_build
%endif

%install
%if %{with python2}
%py2_install
%endif
%if 0%{?with_python3_other}
%py3_other_install
%endif
%py3_install

%if %{with python2}
%files -n python2-%{upstream_name}
%doc README.txt ChangeLog.txt
%license agpl-3.0.txt
%{python2_sitelib}/lrparsing.py*
%{python2_sitelib}/lrparsing*.egg-info
%endif

%files -n python%{python3_pkgversion}-%{upstream_name}
%doc README.txt ChangeLog.txt
%license agpl-3.0.txt
%{python3_sitelib}/lrparsing.py
%{python3_sitelib}/__pycache__/lrparsing.*
%{python3_sitelib}/lrparsing*.egg-info

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{upstream_name}
%doc README.txt ChangeLog.txt
%license agpl-3.0.txt
%{python3_other_sitelib}/lrparsing.py
%{python3_other_sitelib}/__pycache__/lrparsing.*
%{python3_other_sitelib}/lrparsing*.egg-info
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.16-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.16-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.16-2
- Rebuilt for Python 3.8

* Thu Jul 04 2019 Dan Callaghan <dan.callaghan@opengear.com> - 1.0.16-1
- initial version
