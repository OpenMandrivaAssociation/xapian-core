%define oname xapian
%define major 30
%define libname %mklibname %{oname} %{major}
%define develname %mklibname %{oname} -d

Summary:	Search engine library
Name:		xapian-core
Version:	1.4.18
Release:	1
License:	GPLv2+
Group:		Databases
URL:		http://www.xapian.org/
Source0:	http://www.oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	chrpath
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	xapian < 1.0.7
Provides:	xapian = %{version}-%{release}

%description
Xapian is an Open Source Search Engine Library, released under the 
GPL. It's written in C++, with bindings to allow use from Perl, 
Python, PHP, Java, Tcl, C#, and Ruby (so far!)

Xapian is a highly adaptable toolkit which allows developers to easily
add advanced indexing and search facilities to their own applications. 
It supports the Probabilistic Information Retrieval model and also 
supports a rich set of boolean query operators.

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries
Obsoletes:	%{mklibname %{oname} 15} < 1.2.2

%description -n %{libname}
Shared library for %{name}.

%package  -n %{develname}
Summary:	Development files for %{name}
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{oname}-devel = %{version}-%{release}
Provides:	lib%{oname}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{mklibname %{oname} -d -s} < 1.2.17-3

%description -n %{develname}
Development files and headers for %{name}.

%prep
%autosetup -p1

%build
%configure \
%ifarch %{x86_64}
	--enable-sse=sse2 \
%else
	--disable-sse \
%endif
	--enable-shared

%make_build

%install
%make_install

for i in %{buildroot}%{_bindir}/*; do
	# Allow failure for shell scripts
	chrpath -d $i || :
done

%files
%{_bindir}/copydatabase
%{_bindir}/quest
%{_bindir}/simpleexpand
%{_bindir}/simpleindex
%{_bindir}/simplesearch
%{_bindir}/xapian-*
%exclude %{_bindir}/xapian-config
%{_mandir}/man1/*
%{_datadir}/xapian-core

%files -n %{libname}
%{_libdir}/libxapian.so.%{major}*

%files -n %{develname}
%doc %{_docdir}/%{name}/
%dir %{_includedir}/xapian
%{_bindir}/xapian-config
%{_includedir}/xapian/*.h
%{_includedir}/*.h
%{_datadir}/aclocal/xapian.m4
%{_libdir}/libxapian.so
%{_libdir}/cmake/xapian/*.cmake
%{_libdir}/pkgconfig/xapian-core.pc
