
%{!?_licensedir: %global license %%doc}

%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2:        %global __python2 /usr/bin/python2}
%endif

%global modname twiggy
%global distname Twiggy

Name:               python-twiggy
Version:            0.4.7
Release:            20%{?dist}
Summary:            A Pythonic logger

License:            BSD
URL:                http://pypi.python.org/pypi/Twiggy
Source0:            http://pypi.python.org/packages/source/T/%{distname}/%{distname}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python3-sphinx

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-sphinx

%description
Twiggy is a Pythonic logger.

You should use Twiggy because it is awesome. For more information, read the
`documentation <http://twiggy.wearpants.org>`_ or `see this blog post
<http://blog.wearpants.org/meet-twiggy>`_.

%package -n python3-%{modname}
Summary:            A Pythonic logger
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname}
Twiggy is a Pythonic logger.

You should use Twiggy because it is awesome. For more information, read the
`documentation <http://twiggy.wearpants.org>`_ or `see this blog post
<http://blog.wearpants.org/meet-twiggy>`_.

%prep
%autosetup -n %{distname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{distname}.egg-info

%build
%py3_build

%install
%py3_install

# There are errors in the test suite.
#%%check
#./scripts/run-twiggy-tests.sh

%files -n python3-%{modname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{distname}-%{version}-*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.7-20
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.7-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.7-17
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.7-14
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.7-12
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.7-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.7-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 21 2015 Kalev Lember <klember@redhat.com> - 0.4.7-4
- Fix an unexpanded macro

* Mon Nov 16 2015 Ralph Bean <rbean@redhat.com> - 0.4.7-3
- Python3 subpackage and modernize python macros.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 13 2015 Ralph Bean <rbean@redhat.com> - 0.4.7-1
- new version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 01 2013 Ralph Bean <rbean@redhat.com> - 0.4.5-2
- Modernize python rpm macros as per review feedback.

* Thu Oct 31 2013 Ralph Bean <rbean@redhat.com> - 0.4.5-1
- initial package for Fedora
