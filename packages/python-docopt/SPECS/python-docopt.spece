%global pypi_name docopt

Name:           python-docopt
Version:        0.6.2
Release:        17%{?dist}
Summary:        Pythonic argument parser, that will make you smile

License:        MIT
URL:            https://github.com/docopt/docopt
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
Isn't it awesome how optparse and argparse generate help messages
based on your code?!

Hell no! You know what's awesome? It's when the option parser is
generated based on the beautiful help message that you write yourself!
This way you don't need to write thisstupid repeatable parser-code,
and instead can write only the help message--*the way you want it*.

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-%{pypi_name}
Isn't it awesome how optparse and argparse generate help messages
based on your code?!

Hell no! You know what's awesome? It's when the option parser is
generated based on the beautiful help message that you write yourself!
This way you don't need to write thisstupid repeatable parser-code,
and instead can write only the help message--*the way you want it*.

Python 3 version.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
py.test-%{python3_version} -v

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE-MIT
%doc README.rst
%{python3_sitelib}/%{pypi_name}-*.egg-info/
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/__pycache__/%{pypi_name}.*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-15
- Subpackage python2-docopt has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Wed Sep 04 2019 Marek Goldmann <mgoldman@redhat.com> - 0.6.2-14
- Specify better BR for Python 2 packages

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Carl George <carl@george.computer> - 0.6.2-7
- EPEL compatibility, including Python 3 build

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-4
- Rebuild for Python 3.6

* Fri Dec 16 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.2-3
- Don't own __pycache__ directory in python3 subpackage
- Really run tests (setup.py test doesn't do anything)
- Drop copy-pasted Requires (RHBZ #1405639)
- Trivial cleanups

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Germano Massullo <germano.massullo@gmail.com> - 0.6.2-1
- Heavy edits to make spec file compliant to https://fedoraproject.org/wiki/Packaging:Python (package python-docopt did not provide a python2-docopt package in Fedora repositories)
- Removed egg files stuff since they are no longer present in upstream source file.
- 0.6.2 minor update

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Feb 03 2014 Martin Sivak <msivak@redhat.com> - 0.6.1-3
- Fix a mistake in spec file that prevented the subpackage from
  being created for Python 3

* Fri Nov 15 2013 Martin Sivak <msivak@redhat.com> - 0.6.1-2
- Enable python3 package

* Mon Aug 19 2013 Martin Sivak <msivak@redhat.com> - 0.6.1-1
- Upstream version sync

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 14 2013 Martin Sivak <msivak@redhat.com> - 0.5.0-1
- Initial release

