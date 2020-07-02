%global srcname jsonrpclib
%global upstream jsonrpclib-pelix

Name:           python-%{srcname}
Version:        0.3.1
Release:        11%{?dist}
Summary:        JSON-RPC v2.0 client library for Python

License:        ASL 2.0
URL:            http://github.com/tcalmant/jsonrpclib/
Source0:        https://files.pythonhosted.org/packages/source/j/%{upstream}/%{upstream}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description\
This project is an implementation of the JSON-RPC v2.0 specification\
(backwards-compatible) as a client library, for Python 2.7 and Python 3.\
This version is a fork of jsonrpclib by Josh Marshall, usable with Pelix\
remote services.\

%description %_description

%package -n python3-%{srcname}
Summary: %summary
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%setup -q -n %{upstream}-%{version}
rm -rf jsonrpclib_pelix.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/jsonrpclib_pelix-%{version}-py%{python3_version}.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Jonny Heggheim <hegjon@gmail.com> - 0.3.1-5
- Removed Python 2 sub-package
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 09 2017 Jonny Heggheim <hegjon@gmail.com> - 0.3.1-1
- Changed upstream to jsonrpclib-pelix

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.7-5
- Python 2 binary package renamed to python2-jsonrpclib
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Mar 08 2016 Ihar Hrachyshka <ihrachys@redhat.com> 0.1.7-1.el7
- Update to 0.1.7

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec  5 2014 Ihar Hrachyshka <ihrachys@redhat.com> - 0.1.3-2
- Added missing python-setuptools build dependency.
- Added python macros for el6.
- Other stylistic changes.

* Thu Aug  7 2014 Ihar Hrachyshka <ihrachys@redhat.com> - 0.1.3-1
- Initial package for Fedora
