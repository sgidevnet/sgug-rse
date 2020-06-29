%global pname fypp

Name: python-%{pname}
Version: 3.0
Release: 2%{?dist}
Summary: Fortran preprocessor
License: BSD
URL: https://github.com/aradi/fypp
Source0: https://files.pythonhosted.org/packages/source/f/%{pname}/%{pname}-%{version}.tar.gz
# replace env call with direct path to python3
Patch0: python-%{pname}-py3.patch
BuildArch: noarch

%global desc Fypp is a Python powered preprocessor. It can be used for any programming\
languages but its primary aim is to offer a Fortran preprocessor, which helps\
to extend Fortran with condititional compiling and template metaprogramming\
capabilities. Instead of introducing its own expression syntax, it uses Python\
expressions in its preprocessor directives, offering the consistency and\
versatility of Python when formulating metaprogramming tasks. It puts strong\
emphasis on robustness and on neat integration into developing toolchains.

%description
%{desc}

%package -n python3-%{pname}
Summary: %{summary}
BuildRequires: python3-devel
%{?python_provide:%python_provide python3-%{pname}}

%description -n python3-%{pname}
%{desc}

%prep
%autosetup -p1 -n %{pname}-%{version}
rm -rf src/%{pname}.egg-info

%build
%py3_build

%install
%py3_install

%check
test/runtests.sh %{__python3}

%files -n python3-%{pname}
%license LICENSE.txt
%doc CHANGELOG.rst README.rst
%{_bindir}/%{pname}
%{python3_sitelib}/%{pname}.py
%{python3_sitelib}/%{pname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/__pycache__/%{pname}.cpython-%{python3_version_nodots}.opt-1.pyc
%{python3_sitelib}/__pycache__/%{pname}.cpython-%{python3_version_nodots}.pyc

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Dominik Mierzejewski <rpm@greysector.net> 3.0-1
- update to 3.0 (#1790240)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-9
- Rebuilt for Python 3.8

* Sat Aug 10 2019 Dominik Mierzejewski <rpm@greysector.net> 2.1.1-8
- drop unnecessary "cleanup" from prep

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 18 2017 Dominik Mierzejewski <rpm@greysector.net> 2.1.1-2
- fix wrong-script-interpreter/non-executable-script rpmlint error

* Fri Oct 06 2017 Dominik Mierzejewski <rpm@greysector.net> 2.1.1-1
- update to 2.1.1

* Fri Jun 30 2017 Dominik Mierzejewski <rpm@greysector.net> 2.0.1-2
- update upstream URL (bitbucket URL redirects to github)

* Tue Mar 14 2017 Dominik Mierzejewski <rpm@greysector.net> 2.0.1-1
- update to 2.0.1

* Mon Mar 13 2017 Dominik Mierzejewski <rpm@greysector.net> 2.0-1
- initial build
