%global srcname editorconfig
%global sum A Python Based distribution of EditorConfig

Name:           python-%{srcname}
Version:        0.12.0
Release:        18%{?dist}
Summary:        %{sum}

License:        Python and BSD
URL:            http://editorconfig.org
Source0:        https://github.com/editorconfig/editorconfig-core-py/archive/v0.12.0.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-sphinx
BuildRequires:  python3-devel

%description
EditorConfig Python Core provides the same functionality as the EditorConfig C
Core. EditorConfig Python core can be used as a an importable library.

%package     -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
EditorConfig Python Core provides the same functionality as the EditorConfig C
Core. EditorConfig Python core can be used as a an importable library.

%prep
%setup -qn %{srcname}-core-py-%{version}


%build
%{py3_build}
cd docs
make SPHINXBUILD=sphinx-build-3 text

%install
%{py3_install}
mkdir -p $RPM_BUILD_ROOT%{_defaultdocdir}/python3-%{srcname}
cp docs/_build/text/* $RPM_BUILD_ROOT%{_defaultdocdir}/python3-%{srcname}/


# EditorConfig C already places the official binary into /usr/bin.
rm $RPM_BUILD_ROOT%{_bindir}/%{srcname}


%files -n python3-%{srcname}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/*
%{_defaultdocdir}/python3-%{srcname}/*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-18
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-12
- Subpackage python2-editorconfig has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.12.0-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Feb 23 2016 Dennis Chen <barracks510@gmail.com> - 0.12.0-2
- Simplify python package.

* Thu Jan 21 2016 Dennis Chen <barracks510@gmail.com> - 0.12.0-2
- Remove misleading comments and macros.

* Sun Jan 17 2016 Dennis Chen <barracks510@gmail.com> - 0.12.0-1
- First Fedora Packaging.
