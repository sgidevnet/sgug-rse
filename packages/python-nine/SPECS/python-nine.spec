%global modname nine

Name:               python-nine
Version:            1.1.0
Release:            3%{?dist}
Summary:            Python 2 / 3 compatibility, like six, but favouring Python 3

License:            Public Domain
URL:                http://pypi.python.org/pypi/nine
Source0:            https://pypi.python.org/packages/source/n/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:          noarch


BuildRequires:      python3-devel
BuildRequires:      python3-setuptools


%global _description\
Let's write Python 3 right now!\
\
When the best Python 2/Python 3 compatibility modules -- especially the\
famous `*six* library invented by Benjamin Peterson\
<https://pypi.python.org/pypi/six>`_ -- were created, they were written\
from the point of view of a Python 2 programmer starting to grok Python 3.\
\
When thou writeth Python, thou shalt write Python 3 and, just for a while,\
ensure that the thing worketh on Python 2.7 and, possibly, even 2.6.\
\
Just before Python 2 is finally phased out, thine codebase shall look more\
like 3 than like 2.\
\
nine facilitates this new point of view. You can write code that is as\
3ish as possible while still supporting 2.6. Very comfortable for writing\
new projects.

%description %_description

%package -n python3-nine
Summary:            %{summary}
%{?python_provide:%python_provide python3-nine}

%description -n python3-nine  %_description

%prep
%setup -q -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-nine
%doc README.rst
%license LICENSE.rst
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.1.0-1
- Update to upstream, fix python-3.9 build (bz#1792968)
- Removed porting.rst from doc, not available anymore

* Mon Nov 11 2019 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.3.4-21
- Rebuilding package after unretire.

* Mon Sep 16 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-20
- Subpackage python2-nine has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-19
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-15
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.4-14
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.4-12
- Python 2 binary package renamed to python2-nine
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-9
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 12 2015 Ralph Bean <rbean@redhat.com> - 0.3.4-4
- Specify license macro for el6.

* Mon Jan 12 2015 Ralph Bean <rbean@redhat.com> - 0.3.4-3
- Require python-importlib on el6.

* Sat Jan 10 2015 Ralph Bean <rbean@redhat.com> - 0.3.4-2
- Declare noarch.
- Remove unnecessary cflags.
- Remove Group tag, as per review.

* Wed Jan 07 2015 Ralph Bean <rbean@redhat.com> - 0.3.4-1
- initial package for Fedora
