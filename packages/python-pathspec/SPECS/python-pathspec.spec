Name:           python-pathspec
Version:        0.6.0
Release:        3%{?dist}
Summary:        Utility library for gitignore style pattern matching of file paths

License:        MPL 2.0
URL:            https://github.com/cpburnz/python-path-specification
Source0:        https://files.pythonhosted.org/packages/source/p/pathspec/pathspec-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Path Specification (pathspec) is a utility library for pattern matching of file
paths. So far this only includes Git's wildmatch pattern matching which itself
is derived from Rsync's wildmatch. Git uses wildmatch for its gitignore files.

%package -n     python3-pathspec
Summary:        %{summary}
%{?python_provide:%python_provide python3-pathspec}

%description -n python3-pathspec
Path Specification (pathspec) is a utility library for pattern matching of file
paths. So far this only includes Git's wildmatch pattern matching which itself
is derived from Rsync's wildmatch. Git uses wildmatch for its gitignore files.


%prep
%autosetup -n pathspec-%{version}
# Remove bundled egg-info
rm -rf pathspec.egg-info

%build
%py3_build

%install
%py3_install


%check
%{__python3} setup.py test

%files -n python3-pathspec
%doc README.rst
%license LICENSE
%{python3_sitelib}/pathspec
%{python3_sitelib}/pathspec-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Adrien Vergé <adrienverge@gmail.com> - 0.6.0-1
- Update to latest upstream version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.3-7
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.3-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 7 2017 Adrien Vergé <adrienverge@gmail.com> - 0.5.3-1
- Update to latest upstream version
- Include LICENSE file now that upstream packages it

* Wed Jun 28 2017 Adrien Vergé <adrienverge@gmail.com> - 0.5.2-1
- Initial package.
