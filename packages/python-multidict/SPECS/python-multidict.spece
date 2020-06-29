%global modname multidict
#global rctag b4

Name:           python-%{modname}
Version:        4.7.6%{?rctag:~%{rctag}}
Release:        2%{?dist}
Summary:        MultiDict implementation

License:        ASL 2.0
URL:            https://github.com/aio-libs/multidict
Source0:        %{url}/archive/v%{version}%{?rctag:%{rctag}}/%{modname}-%{version}%{?rctag:%{rctag}}.tar.gz

BuildRequires:  gcc

%global _description \
Multidicts are useful for working with HTTP headers, URL query args etc.\
\
The code was extracted from aiohttp library.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname} %{_description}

%prep
%autosetup -n %{modname}-%{version}%{?rctag:%{rctag}}
sed -i -e '/addopts/d' setup.cfg

%build
%py3_build

%install
%py3_install
rm -vf %{buildroot}%{python3_sitearch}/%{modname}/*.{c,pyx}

%check
PYTHONPATH=%{buildroot}%{python3_sitearch} pytest-%{python3_version} -v tests

%files -n python3-%{modname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{modname}-*.egg-info/
%{python3_sitearch}/%{modname}/

%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 4.7.6-2
- Rebuilt for Python 3.9

* Sat May 16 2020 Fabian Affolter  <mail@fabian-affolter.ch> - 4.7.6-1
- Update to latest upstream release 4.7.6 (rhbz#1836076)

* Sat Feb 22 2020 Fabian Affolter  <mail@fabian-affolter.ch> - 4.7.5-1
- Update to latest upstream release 4.7.5 (rhbz#1806083)

* Mon Feb 03 2020 Fabian Affolter  <mail@fabian-affolter.ch> - 4.7.4-1
- UPdate to latest upstream release 4.7.4 (rhbz#1774256)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.5.2-1
- Update to 4.5.2

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 4.3.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.3.1-1
- Update to 4.3.1

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.1.0-1
- Update to 4.1.0

* Mon Jan 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.0.0-1
- Update to 4.0.0

* Fri Nov 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.3.2-1
- Update to 3.3.2

* Thu Nov 02 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.3.1-1
- Update to 3.3.1

* Fri Oct 20 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.3.0-1
- Update to 3.3.0

* Sun Oct 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 16 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.3-1
- Update to 3.1.3

* Mon Jul 03 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0
- Ignore tests until imports are fixed

* Thu Jun 08 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.6-1
- Update to 2.1.6

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.4-1.1
- Rebuild for Python 3.6

* Thu Dec 01 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.1.4-1
- Update to 2.1.4

* Thu Dec 01 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.1.3-1
- Update to 2.1.3

* Mon Nov 07 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.1.2-1
- Update to 2.1.2

* Fri Sep 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.1.1-1
- Update to 2.1.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-1.1
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jul 07 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.1.0-1
- Update to 1.1.0
- Trivial fixes

* Thu Jun 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.1.0-0.1b4
- Initial package
