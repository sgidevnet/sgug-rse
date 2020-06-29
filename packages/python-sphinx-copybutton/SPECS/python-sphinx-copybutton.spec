%global srcname sphinx-copybutton

Name:           python-%{srcname}
Version:        0.2.12
Release:        1%{?dist}
Summary:        Add a copy button to code cells in Sphinx docs

License:        MIT
URL:            https://sphinx-copybutton.readthedocs.io/en/latest/
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-ipython-sphinx

%global _description %{expand:
Sphinx-copybutton does one thing: add a little "copy" button to the
right of your code blocks.  If the code block overlaps to the right of
the text area, you can just click the button to get the whole thing.}

%description
%_description

%package     -n python3-%{srcname}
Summary:        Add a copy button to code cells in Sphinx docs
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%_description

%package        doc
Summary:        Documentation for %{srcname}

%description    doc
Documentation for %{srcname}.

%prep
%autosetup -n %{srcname}-%{version}

# Remove spurious executable bits
find -O3 . -type f -perm /0111 -exec chmod a-x {} \+

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

# Build the documentation
PYTHONPATH=$PWD make -C doc html
rm doc/_build/html/.buildinfo

%install
%pyproject_install

%check
%tox

%files       -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/sphinx_copybutton*

%files          doc
%doc doc/_build/html
%license LICENSE

%changelog
* Wed Jun 17 2020 Jerry James <loganjerry@gmail.com> - 0.2.12-1
- Version 0.2.12

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.11-2
- Rebuilt for Python 3.9

* Thu Apr 23 2020 Jerry James <loganjerry@gmail.com> - 0.2.11-1
- Version 0.2.11

* Thu Apr  2 2020 Jerry James <loganjerry@gmail.com> - 0.2.10-1
- Version 0.2.10

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec  6 2019 Jerry James <loganjerry@gmail.com> - 0.2.6-2
- Ship the LICENSE file with the -doc subpackage too

* Thu Dec  5 2019 Jerry James <loganjerry@gmail.com> - 0.2.6-1
- Initial RPM
