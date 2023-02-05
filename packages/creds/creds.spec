%global bashcompdir %(pkg-config --variable=completionsdir bash-completion)
%global zshcompdir %{_datadir}/zsh/site-functions

Name: creds
Version: 0.1.0
Release: 2%{?dist}
Summary: Simple encrypted credential management with GPG

License: ASL 2.0
URL: https://github.com/joemiller/creds
Source0: https://github.com/joemiller/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: bash-completion

Requires: gnupg2

%description
Simple encrypted credential management with GPG.


%prep
%autosetup
# Remove shebang from Bash completion file.
sed -i -e '/^#!\//, 1d' completions/bash/_%{name}.sh


%build


%install
# NOTE: creds comes with a Makefile, but the paths therein are hard-coded which
# makes it unsuitable for RPM packaging purposes.
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 %{name} %{buildroot}%{_bindir}

# Install Bash/Zsh completion files.
mkdir -p %{buildroot}%{bashcompdir}
mv completions/bash/_%{name}.sh %{buildroot}%{bashcompdir}/%{name}
mkdir -p %{buildroot}%{zshcompdir}
mv completions/zsh/_%{name}.sh %{buildroot}%{zshcompdir}/_%{name}


%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{bashcompdir}/%{name}
# Since Zsh is not a requirement for this package, it must own all the
# directories below %%{_datadir} to avoid unowned directories.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/UnownedDirectories/
%dir %(dirname %{zshcompdir})
%dir %{zshcompdir}
%{zshcompdir}/_%{name}


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Tadej Janež <tadej.j@nez.si> - 0.1.0-1
- Initial package
