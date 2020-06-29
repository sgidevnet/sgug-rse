%global srcname pipreqs

%global _description\
This library generates a 'requirements.txt' file for any Python project based \
on import statements of the project. It does not need the packages to be \
installed in the environment for creating the requirements file. It traverses \
through the files in the projects, finds the import statements and generates \
the output file.

Name:           python-%{srcname}
Version:        0.4.9
Release:        6%{?dist}
Summary:        Pip requirements.txt generator based on imports in project

License:        ASL 2.0
URL:            https://github.com/bndr/pipreqs
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist docopt}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist yarg}
BuildRequires:  %{py3_dist sphinx}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%{?python_enable_dependency_generator}
%description -n python3-%{srcname} %_description

%package -n python-%{srcname}-doc
Summary: Documentation for pipreqs
%description -n python-%{srcname}-doc
Documentation for the pipreqs tool.

%prep
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
sphinx-build -b man docs build/man/
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install
install -Dm0644 -p build/man/pipreqs.1 -t %buildroot/%_mandir/man1/
# Remove shebang lines from python files
for lib in %{buildroot}%{python3_sitelib}/%{srcname}/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

# Checks are disabled because it tries to access pypi.python.org over the
# interwebz which fails.

# check
# {__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc docs/readme.rst README.rst
%{_bindir}/pipreqs
%{_mandir}/man1/pipreqs.1*
# Ignore tests
%exclude %{python3_sitelib}/tests
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info

%files -n python-%{srcname}-doc
%doc html

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.9-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.9-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.9-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 24 2018 Dhanesh B. Sabane <dhanesh95@disroot.org> - 0.4.9-1
- Initial package.
