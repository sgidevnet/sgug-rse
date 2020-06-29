%global srcname fuckit

Name:           python-%{srcname}
Version:        4.8.0
Release:        22%{?dist}
Summary:        The Python Error Steamroller

License:        WTFPL
URL:            https://github.com/ajalt/fuckitpy
Source0:        https://pypi.python.org/packages/source/f/fuckit/fuckit-4.8.0.zip

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose

%global _description\
FuckIt.py uses state-of-the-art technology to make sure your Python code runs\
whether it has any right to or not. Some code has an error? Fuck it.\


%description %_description


%package -n python3-%{srcname}
Summary:        The Python Error Steamroller
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
FuckIt.py uses state-of-the-art technology to make sure your Python code runs
whether it has any right to or not. Some code has an error? Fuck it.


%prep
%setup -qn %{srcname}-%{version}

find -name '*.txt' | xargs chmod -x
find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-%{srcname}
# The license text is available in README.md
%doc README.md
%{python3_sitelib}/%{srcname}.py*
%{python3_sitelib}/__pycache__/%{srcname}.*
%{python3_sitelib}/%{srcname}-%{version}*.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.8.0-22
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.8.0-20
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.8.0-19
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Miro Hrončok <mhroncok@redhat.com> - 4.8.0-16
- Drop the python2 subpackage (#1627369)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.8.0-14
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.8.0-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.8.0-11
- Python 2 binary package renamed to python2-fuckit
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Igor Gnatenko <ignatenko@redhat.com> - 4.8.0-9
- Rebuild for brp-python-bytecompile

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.8.0-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 10 2014 Ian Weller <ian@ianweller.org> - 4.8.0-2
- Only build for Python 3 on EPEL

* Mon Sep 15 2014 Ian Weller <ian@ianweller.org> - 4.8.0-1
- Update to 4.8.0 and fix packaging concerns

* Fri Dec 06 2013 Ian Weller <iweller@redhat.com> - 1.0.0-1.20131206gitb8cf18f
- Initial package build
