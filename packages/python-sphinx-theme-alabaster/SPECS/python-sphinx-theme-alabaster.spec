%global pypi_name alabaster
%global srcname sphinx-theme-%{pypi_name}

Name:           python-%{srcname}
Version:        0.7.12
Release:        5%{?dist}
Summary:        Configurable sidebar-enabled Sphinx theme

License:        BSD
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/cc/b4/ed8dcb0d67d5cfb7f83c4d5463a7614cb1d078ad7ae890c9143edebbf072/alabaster-0.7.12.tar.gz

BuildArch:      noarch

%description
This theme is a modified "Kr" Sphinx theme from @kennethreitz (especially as
used in his Requests project), which was itself originally based on @mitsuhiko's
theme used for Flask & related projects.


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        Configurable sidebar-enabled Sphinx theme
BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
This theme is a modified "Kr" Sphinx theme from @kennethreitz (especially as
used in his Requests project), which was itself originally based on @mitsuhiko's
theme used for Flask & related projects.


%prep
%setup -qn %{pypi_name}-%{version}

# Remove bundled eggs
rm -rf %{pypi_name}.egg-info


%build
%py3_build


%install
%py3_install


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{pypi_name}/


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 06 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.12-4
- Subpackage python2-sphinx-theme-alabaster has been removed
  See https://fedoraproject.org/wiki/Changes/Sphinx2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 06 2018 Julien Enselme <jujens@jujens.eu> - 0.7.12-2
- Readd Python 2 subpackage

* Thu Oct 04 2018 Julien Enselme <jujens@jujens.eu> - 0.7.12-1
- Update to 0.7.12
- Remove Python 2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.11-4
- Rebuilt for Python 3.7

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.11-3
- Rebuilt for Python 3.7

* Sat Jun 30 2018 Julien Enselme <jujens@jujens.eu> - 0.7.11-2
- Correct source URL

* Sat Jun 30 2018 Julien Enselme <jujens@jujens.eu> - 0.7.11-1
- Update to 0.7.11

* Thu Jun 14 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.9-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.7.9-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.7.9-2
- Rebuild for Python 3.6

* Sun Sep 18 2016 Julien Enselme <jujens@jujens.eu> - 0.7.9-1
- Update to 0.7.9

* Fri May 13 2016 Julien Enselme <jujens@jujens.eu> - 0.7.8-1
- Use %%python3_pkgversion macro for EPEL7 release

* Fri May 13 2016 Julien Enselme <jujens@jujens.eu> - 0.7.8-1
- Update to 0.7.8 (#1334952)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 5 2015 Julien Enselme <jujens@jujens.eu> - 0.7.6-5
- Rebuilt for python 3.5

* Fri Jul 31 2015 Julien Enseme <jujens@jujens.eu> - 0.7.6-4
- Use %%py2_build, %%py3build, %%py2_install and %%py2_install
- Make a python2 subpackage

* Thu Jul 30 2015 Julien Enselme <jujens@jujens.eu> - 0.7.6-3
- Add provides for python2-sphinx-theme-alabaster
- Remove usage of python2 and python3 dirs

* Fri Jul 24 2015 Julien Enselme <jujens@jujens.eu> - 0.7.6-2
- Remove %%py3dir macro
- Add CFLAGS in %%build

* Sat Jul 18 2015 Julien Enselme <jujens@jujens.eu> - 0.7.6-1
- Initial packaging
